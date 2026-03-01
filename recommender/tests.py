"""
Comprehensive test suite for Movie Recommendation System
"""
from django.test import TestCase, Client
from django.urls import reverse
import json


class HomePageTests(TestCase):
    """Tests for the home page"""
    
    def setUp(self):
        self.client = Client()
    
    def test_home_page_loads(self):
        """Test that home page loads successfully"""
        response = self.client.get(reverse('recommender:main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Movie Recommendation System')
    
    def test_home_page_has_search_form(self):
        """Test that home page contains search form"""
        response = self.client.get(reverse('recommender:main'))
        self.assertContains(response, 'movie_name')
        self.assertContains(response, 'Get Recommendations')
    
    def test_home_page_shows_movie_count(self):
        """Test that home page displays movie count"""
        response = self.client.get(reverse('recommender:main'))
        self.assertContains(response, 'movies available')


class SearchAPITests(TestCase):
    """Tests for the search API endpoint"""
    
    def setUp(self):
        self.client = Client()
    
    def test_search_api_valid_query(self):
        """Test search API with valid query"""
        response = self.client.get('/api/search/?q=matrix')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('movies', data)
        self.assertIn('count', data)
        self.assertIsInstance(data['movies'], list)
        self.assertIsInstance(data['count'], int)
    
    def test_search_api_short_query(self):
        """Test search API with query too short"""
        response = self.client.get('/api/search/?q=a')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['count'], 0)
        self.assertEqual(data['movies'], [])
    
    def test_search_api_empty_query(self):
        """Test search API with empty query"""
        response = self.client.get('/api/search/?q=')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['count'], 0)
    
    def test_search_api_no_query_param(self):
        """Test search API without query parameter"""
        response = self.client.get('/api/search/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['count'], 0)
    
    def test_search_api_special_characters(self):
        """Test search API with special characters"""
        response = self.client.get('/api/search/?q=test@#$')
        self.assertEqual(response.status_code, 200)
        # Should not crash, just return empty or filtered results


class HealthCheckTests(TestCase):
    """Tests for the health check endpoint"""
    
    def setUp(self):
        self.client = Client()
    
    def test_health_check_endpoint_exists(self):
        """Test that health check endpoint is accessible"""
        response = self.client.get('/api/health/')
        self.assertIn(response.status_code, [200, 503])
    
    def test_health_check_response_format(self):
        """Test health check response has correct format"""
        response = self.client.get('/api/health/')
        data = json.loads(response.content)
        self.assertIn('status', data)
        
        if response.status_code == 200:
            self.assertEqual(data['status'], 'healthy')
            self.assertIn('movies_loaded', data)
            self.assertIn('model_dir', data)
            self.assertIn('model_loaded', data)


class ModelStatusTests(TestCase):
    """Tests for the model status endpoint"""
    
    def setUp(self):
        self.client = Client()
    
    def test_model_status_endpoint_exists(self):
        """Test that model status endpoint is accessible"""
        response = self.client.get('/api/model-status/')
        self.assertEqual(response.status_code, 200)
    
    def test_model_status_response_format(self):
        """Test model status response has correct format"""
        response = self.client.get('/api/model-status/')
        data = json.loads(response.content)
        self.assertIn('loaded', data)
        self.assertIn('progress', data)
        self.assertIn('status', data)
        
        # Status should be one of the expected values
        self.assertIn(data['status'], ['ready', 'loading', 'initializing', 'error'])


class RecommendationTests(TestCase):
    """Tests for the recommendation functionality"""
    
    def setUp(self):
        self.client = Client()
    
    def test_post_recommendation_without_movie_name(self):
        """Test POST request without movie name"""
        response = self.client.post(reverse('recommender:main'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a movie name')
    
    def test_post_recommendation_with_empty_movie_name(self):
        """Test POST request with empty movie name"""
        response = self.client.post(reverse('recommender:main'), {
            'movie_name': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a movie name')
    
    def test_post_recommendation_with_whitespace_only(self):
        """Test POST request with whitespace-only movie name"""
        response = self.client.post(reverse('recommender:main'), {
            'movie_name': '   '
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a movie name')
    
    def test_csrf_token_required(self):
        """Test that CSRF token is required for POST requests"""
        # This should fail without CSRF token
        client = Client(enforce_csrf_checks=True)
        response = client.post(reverse('recommender:main'), {
            'movie_name': 'The Matrix'
        })
        self.assertEqual(response.status_code, 403)


class URLRoutingTests(TestCase):
    """Tests for URL routing"""
    
    def test_main_url_resolves(self):
        """Test that main URL resolves correctly"""
        url = reverse('recommender:main')
        self.assertEqual(url, '/')
    
    def test_search_url_exists(self):
        """Test that search API URL exists"""
        response = self.client.get('/api/search/?q=test')
        self.assertNotEqual(response.status_code, 404)
    
    def test_health_url_exists(self):
        """Test that health check URL exists"""
        response = self.client.get('/api/health/')
        self.assertNotEqual(response.status_code, 404)
    
    def test_model_status_url_exists(self):
        """Test that model status URL exists"""
        response = self.client.get('/api/model-status/')
        self.assertNotEqual(response.status_code, 404)


class SecurityTests(TestCase):
    """Security-related tests"""
    
    def setUp(self):
        self.client = Client()
    
    def test_xss_protection_in_search(self):
        """Test that XSS attempts are escaped"""
        response = self.client.post(reverse('recommender:main'), {
            'movie_name': '<script>alert("XSS")</script>'
        })
        self.assertEqual(response.status_code, 200)
        # Django should escape the script tag
        self.assertNotContains(response, '<script>alert("XSS")</script>', html=False)
    
    def test_sql_injection_protection(self):
        """Test that SQL injection attempts are handled safely"""
        response = self.client.get('/api/search/?q=\' OR 1=1--')
        self.assertEqual(response.status_code, 200)
        # Should not crash or expose data
    
    def test_csrf_protection_enabled(self):
        """Test that CSRF protection is enabled"""
        response = self.client.get(reverse('recommender:main'))
        self.assertContains(response, 'csrfmiddlewaretoken')


class ResponseHeaderTests(TestCase):
    """Tests for security headers"""
    
    def setUp(self):
        self.client = Client()
    
    def test_content_type_header(self):
        """Test that content-type header is set correctly"""
        response = self.client.get(reverse('recommender:main'))
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
    
    def test_json_content_type_for_api(self):
        """Test that API endpoints return JSON content type"""
        response = self.client.get('/api/search/?q=test')
        self.assertIn('application/json', response['Content-Type'])


class ErrorHandlingTests(TestCase):
    """Tests for error handling"""
    
    def setUp(self):
        self.client = Client()
    
    def test_404_page_not_found(self):
        """Test that 404 errors are handled"""
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
    
    def test_invalid_method_on_api(self):
        """Test that invalid HTTP methods are rejected"""
        response = self.client.put('/api/search/?q=test')
        self.assertEqual(response.status_code, 405)  # Method Not Allowed
    
    def test_post_to_get_only_endpoint(self):
        """Test POST to GET-only endpoint"""
        response = self.client.post('/api/search/', {'q': 'test'})
        self.assertEqual(response.status_code, 405)


class PerformanceTests(TestCase):
    """Basic performance tests"""
    
    def setUp(self):
        self.client = Client()
    
    def test_home_page_response_time(self):
        """Test that home page responds quickly"""
        import time
        start = time.time()
        response = self.client.get(reverse('recommender:main'))
        duration = time.time() - start
        
        self.assertEqual(response.status_code, 200)
        # Should respond in less than 2 seconds
        self.assertLess(duration, 2.0)
    
    def test_api_response_time(self):
        """Test that API responds quickly"""
        import time
        start = time.time()
        response = self.client.get('/api/search/?q=matrix')
        duration = time.time() - start
        
        self.assertEqual(response.status_code, 200)
        # Should respond in less than 1 second
        self.assertLess(duration, 1.0)


class IntegrationTests(TestCase):
    """Integration tests for complete workflows"""
    
    def setUp(self):
        self.client = Client()
    
    def test_complete_search_workflow(self):
        """Test complete search workflow from home to results"""
        # 1. Load home page
        response = self.client.get(reverse('recommender:main'))
        self.assertEqual(response.status_code, 200)
        
        # 2. Search for movies via API
        response = self.client.get('/api/search/?q=matrix')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        
        # 3. If movies found, submit recommendation request
        if data['count'] > 0:
            movie_name = data['movies'][0]
            response = self.client.post(reverse('recommender:main'), {
                'movie_name': movie_name
            })
            # Should either show results or error (both are 200)
            self.assertEqual(response.status_code, 200)
    
    def test_health_check_before_search(self):
        """Test checking health before performing search"""
        # 1. Check health
        response = self.client.get('/api/health/')
        
        # 2. If healthy, perform search
        if response.status_code == 200:
            response = self.client.get('/api/search/?q=test')
            self.assertEqual(response.status_code, 200)


# Run tests with: python manage.py test recommender
# Run specific test: python manage.py test recommender.tests.HomePageTests
# Run with verbose output: python manage.py test --verbosity=2
