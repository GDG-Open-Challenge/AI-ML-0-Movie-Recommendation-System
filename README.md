<div align="center">

# 🎬 Movie Recommendation System

> A production-ready, AI-powered movie recommendation system built with Django and advanced machine learning. Scalable from thousands to millions of movies.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://djangoproject.com/)
[![scikit--learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[Features](#-features) • [Quick Start](#-quick-start) • [Demo](#-screenshots--demo) • [Documentation](#-documentation) • [API](#-api-reference)

</div>

---

![Logo Image](./assets/images-for-readme/Logo.png)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Screenshots](#-screenshots)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Model Training](#-model-training)
- [API Reference](#-api-reference)
- [Configuration](#-configuration)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The Movie Recommendation System provides intelligent movie suggestions using **content-based filtering** with TF-IDF vectorization and SVD dimensionality reduction. It features a modern web interface, RESTful API, and supports datasets from 2K to 1M+ movies with sub-50ms recommendation generation.

![Header Image](./assets/images-for-readme/Header.png)

### 🌟 Why This Project?

- ✅ **Production Ready** - Security hardened, optimized, well-documented with comprehensive error handling
- ✅ **Scalable Architecture** - Handles millions of movies efficiently with memory-optimized data structures
- ✅ **Modern Tech Stack** - Django 6.0, Python 3.11+, scikit-learn, advanced ML pipelines
- ✅ **Easy to Use** - Simple installation, clear documentation, demo model included
- ✅ **Flexible** - Train your own models or use pre-trained demo models
- ✅ **API First** - RESTful endpoints for easy integration with other applications
- ✅ **Developer Friendly** - Clean code, comprehensive documentation, easy to extend

### 🛠️ Key Technologies

| Category | Technologies |
|----------|-------------|
| **Backend** | Django 6.0, Python 3.11+ |
| **ML/Data Science** | scikit-learn, pandas, numpy, scipy |
| **Machine Learning** | TF-IDF Vectorization, SVD Dimensionality Reduction, Cosine Similarity |
| **Storage** | Parquet (efficient columnar format), SQLite/PostgreSQL |
| **Deployment** | Render, Heroku, Docker, AWS compatible |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |

### 🎓 How It Works

The recommendation engine uses a sophisticated content-based filtering approach:

1. **Feature Extraction**: Combines movie metadata (genres, keywords, cast, crew) into rich text features
2. **TF-IDF Vectorization**: Converts text features into numerical vectors with importance weighting
3. **Dimensionality Reduction**: Uses SVD to reduce vector dimensions while preserving similarity relationships
4. **Similarity Computation**: Calculates cosine similarity between all movie pairs
5. **Fast Retrieval**: Returns top-N most similar movies in under 50ms

---

## 📸 Screenshots & Demo

### Demo Video

![Application Demo](./assets/demo-video/Application-Demo.gif)

### Model Loading

![Model Loading](./assets//images-for-readme/Loading.png)

### Home Page

![Home Page](./assets/images-for-readme/Homepage.png)

### Movie Search Recommendations

![Movie Recommendations](./assets/images-for-readme/Results.png)

---

## ✨ Features

### 👤 User Features
- 🔍 **Smart Search** - Real-time autocomplete with fuzzy matching and typo tolerance
- 🎬 **AI Recommendations** - Content-based filtering with 15+ personalized suggestions
- ⭐ **Rich Metadata** - Ratings, votes, genres, production companies, release dates
- 🔗 **External Links** - Direct Google Search and IMDb integration for each movie
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- ⚡ **Fast Performance** - Sub-50ms recommendation generation, sub-100ms search
- 🎨 **Modern UI** - Clean, intuitive interface with smooth animations
- 🌐 **No Login Required** - Instant access without registration

### 🔧 Technical Features
- 🤖 **Advanced ML** - TF-IDF vectorization + SVD dimensionality reduction
- 📊 **Highly Scalable** - Handles 2K to 1M+ movies with optimized memory usage
- 💾 **Efficient Storage** - Parquet format with compression (5-10x smaller than CSV)
- 🔧 **Configurable** - Easy model switching via `MODEL_DIR` environment variable
- 📡 **REST API** - JSON endpoints for seamless integration with other apps
- 🔒 **Secure** - Production-ready security settings, CSRF protection, SQL injection prevention
- 📝 **Comprehensive Logging** - Detailed error tracking and performance monitoring
- 🚀 **Deployment Ready** - Render, Heroku, Docker, AWS configurations included
- 🧪 **Quality Filtering** - Configurable thresholds for vote count and rating
- 🔄 **Hot Reload** - Model updates without server restart
- 📈 **Performance Metrics** - Built-in health check and monitoring endpoints

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher ([Download](https://www.python.org/downloads/))
- pip package manager (included with Python)
- 8GB RAM minimum (16GB recommended for training large datasets)
- Git ([Download](https://git-scm.com/downloads))
- 2GB free disk space (more for larger models)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up environment variables (optional for development)
cp .env.example .env
# Edit .env and set SECRET_KEY (or use default for development)

# 6. Run database migrations
python manage.py migrate

# 7. Start the development server
python manage.py runserver
```

### Access the Application

Open your browser and navigate to:
```
http://localhost:8000
```

That's it! The demo model (2K movies) is included and works out of the box. 🎉

### Verify Installation

Check if everything is working:

```bash
# Health check endpoint
curl http://localhost:8000/api/health/

# Expected response:
# {"status": "healthy", "movies_loaded": 2000, "model_loaded": true}
```

### Troubleshooting Installation

If you encounter issues:

```bash
# Check Python version
python --version  # Should be 3.11+

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies with verbose output
pip install -r requirements.txt -v

# Check for port conflicts
netstat -an | grep 8000
```

For more help, see [PROJECT_GUIDE.md - Troubleshooting](PROJECT_GUIDE.md#-troubleshooting)

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── 📚 Documentation
│   ├── README.md                  # This file - overview and quick start
│   ├── PROJECT_GUIDE.md           # Complete technical guide
│   └── CHANGELOG.md               # Version history and changes
│
├── ⚙️ Django Application
│   ├── movie_recommendation/      # Django project settings
│   │   ├── settings.py           # Configuration
│   │   ├── urls.py               # URL routing
│   │   └── wsgi.py               # WSGI entry point
│   │
│   ├── recommender/              # Main application
│   │   ├── views.py              # Recommendation logic
│   │   ├── urls.py               # App URLs
│   │   └── templates/            # HTML templates
│   │       └── recommender/
│   │           ├── index.html    # Search page
│   │           ├── result.html   # Results page
│   │           └── error.html    # Error page
│   │
│   ├── manage.py                 # Django management script
│   └── requirements.txt          # Python dependencies
│
├── 🎓 Model Training
│   └── training/
│       ├── train.py              # Training pipeline
│       ├── infer.py              # Inference examples
│       └── guide.md              # Training documentation
│
├── 🎯 Models (Created after training)
│   └── models/
│       ├── movie_metadata.parquet    # Movie information
│       ├── similarity_matrix.npz     # Similarity scores
│       ├── title_to_idx.json         # Title mappings
│       ├── tfidf_vectorizer.pkl      # TF-IDF model
│       └── svd_model.pkl             # SVD reduction model
│
├── 📦 Static Files
│   └── static/
│       ├── logo.png                  # Application logo
│       ├── demo_model.parquet        # Demo similarity model (2K)
│       └── top_2k_movie_data.parquet # Demo movie data (2K)
│
└── 🚀 Deployment
    ├── Procfile                  # Heroku configuration
    ├── render.yaml               # Render configuration
    └── .gitignore                # Git ignore rules
```

---

## 💡 Usage

### Web Interface

1. **Search for a Movie**
   - Navigate to `http://localhost:8000`
   - Start typing a movie name in the search box
   - Select from autocomplete suggestions or type the full name
   - The search supports partial matches and typo tolerance

2. **View Recommendations**
   - Click "Get Recommendations" button
   - Browse 15 similar movie suggestions ranked by relevance
   - Each card displays:
     - Movie title and release year
     - Average rating (⭐) and vote count
     - Genres and production company
     - Quick action buttons

3. **Explore Movies**
   - Click "Google" to search for the movie online
   - Click "IMDb" to view detailed information on IMDb (if available)
   - Hover over cards for smooth animations and effects

### Example Searches

Try these popular movies to see the system in action:

- "The Dark Knight" → Get superhero/action recommendations
- "Inception" → Discover mind-bending thrillers
- "The Shawshank Redemption" → Find dramatic masterpieces
- "Toy Story" → Explore animated family films
- "Pulp Fiction" → Get crime/drama suggestions

### API Usage

The system provides RESTful API endpoints for programmatic access.

#### Search Movies (Autocomplete)

```bash
# Basic search
curl "http://localhost:8000/api/search/?q=matrix"

# Response
{
  "movies": ["The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"],
  "count": 3
}
```

#### Get Recommendations (Programmatic)

```bash
# POST request with movie title
curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "movie_name=Inception"

# Returns HTML with recommendations
```

#### Health Check

```bash
# Check system status
curl http://localhost:8000/api/health/

# Response
{
  "status": "healthy",
  "movies_loaded": 100000,
  "model_dir": "./models",
  "model_loaded": true,
  "memory_usage_mb": 245.6,
  "uptime_seconds": 3600
}
```

#### Python Integration Example

```python
import requests

# Search for movies
response = requests.get('http://localhost:8000/api/search/', params={'q': 'inception'})
movies = response.json()['movies']
print(f"Found {len(movies)} movies")

# Check health
health = requests.get('http://localhost:8000/api/health/').json()
print(f"System status: {health['status']}")
print(f"Movies loaded: {health['movies_loaded']}")
```

---

## 🎓 Model Training

### Using Demo Model

The project includes a pre-trained demo model with 2,000 popular movies. No training needed!

```bash
# Demo model is in static/ directory
export MODEL_DIR=./static
python manage.py runserver
```

### Training Your Own Model

Want to train on more movies or your own dataset? See the [**Training Guide**](training/guide.md) for:

- 📖 Complete training documentation
- 🎯 Configuration options (10K to 1M+ movies)
- ⚙️ Performance tuning guidelines
- 📊 Dataset requirements
- 🔧 Advanced features

**Quick Training Example:**

```python
from training.train import MovieRecommenderTrainer

# Initialize trainer
trainer = MovieRecommenderTrainer(
    output_dir='./models',
    use_dimensionality_reduction=True,
    n_components=500
)

# Train on your dataset
df, sim_matrix = trainer.train(
    'path/to/your/dataset.csv',
    quality_threshold='medium',  # low/medium/high
    max_movies=100000            # Limit dataset size
)
```

**For detailed training instructions**, see:
- 📘 [Training Guide](training/guide.md) - Complete training documentation
- 📘 [PROJECT_GUIDE.md](PROJECT_GUIDE.md#-model-training) - Training setup and configurations

---

## 📡 API Reference

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with search interface |
| `/` | POST | Submit movie search and get recommendations |
| `/api/search/` | GET | Search movies (autocomplete) |
| `/api/health/` | GET | Health check endpoint |

### Search Movies

**Request:**
```http
GET /api/search/?q=inception
```

**Response:**
```json
{
  "movies": ["Inception", "Inception: The Cobol Job"],
  "count": 2
}
```

### Health Check

**Request:**
```http
GET /api/health/
```

**Response:**
```json
{
  "status": "healthy",
  "movies_loaded": 100000,
  "model_dir": "./models",
  "model_loaded": true
}
```

For complete API documentation, see [PROJECT_GUIDE.md - API Reference](PROJECT_GUIDE.md#-api-reference)

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file (optional for development):

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Model Configuration
MODEL_DIR=./models

# Database (optional - defaults to SQLite)
# DATABASE_URL=postgresql://user:password@localhost/dbname

# Deployment
# RENDER_EXTERNAL_HOSTNAME=your-app.onrender.com
```

### Using Different Models

To switch between models, set the `MODEL_DIR` environment variable:

```bash
# Use demo model (2K movies)
export MODEL_DIR=./static

# Use your trained model (custom)
export MODEL_DIR=./models

# Use absolute path
export MODEL_DIR=/path/to/your/models
```

For detailed configuration options, see [PROJECT_GUIDE.md - Configuration](PROJECT_GUIDE.md#-configuration)

---

## 📚 Documentation

### Main Documentation

- **[README.md](README.md)** (this file) - Overview, quick start, basic usage
- **[PROJECT_GUIDE.md](PROJECT_GUIDE.md)** - Complete technical guide
  - Installation
  - Model training
  - Configuration
  - Development
  - Deployment
  - API reference
  - Troubleshooting
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and changes

### Training Documentation

- **[training/guide.md](training/guide.md)** - Complete model training guide
  - Dataset requirements
  - Training configurations
  - Performance tuning
  - Advanced features

### Quick Links

| Topic | Documentation |
|-------|---------------|
| Installation | [Quick Start](#-quick-start) or [PROJECT_GUIDE.md](PROJECT_GUIDE.md#-installation) |
| Model Training | [training/guide.md](training/guide.md) |
| Deployment | [PROJECT_GUIDE.md - Deployment](PROJECT_GUIDE.md#-deployment) |
| API Reference | [API Reference](#-api-reference) or [PROJECT_GUIDE.md](PROJECT_GUIDE.md#-api-reference) |
| Troubleshooting | [PROJECT_GUIDE.md - Troubleshooting](PROJECT_GUIDE.md#-troubleshooting) |
| Configuration | [Configuration](#-configuration) or [PROJECT_GUIDE.md](PROJECT_GUIDE.md#-configuration) |

---

## 🚀 Deployment

### Quick Deploy to Render

1. Push your code to GitHub
2. Connect repository to [Render](https://render.com)
3. Render auto-detects `render.yaml`
4. Set environment variables
5. Deploy!

### Other Platforms

- **Heroku**: Uses `Procfile`
- **Docker**: Create Dockerfile from PROJECT_GUIDE
- **AWS**: Elastic Beanstalk compatible
- **Digital Ocean**: App Platform ready

For detailed deployment instructions, see [PROJECT_GUIDE.md - Deployment](PROJECT_GUIDE.md#-deployment)

---

## 🤝 Contributing

Contributions are welcome! We appreciate your help in making this project better.

### How to Contribute

1. **Fork the repository** - Click the "Fork" button at the top right
2. **Clone your fork** - `git clone https://github.com/yourusername/movie-recommendation-system.git`
3. **Create a feature branch** - `git checkout -b feature/amazing-feature`
4. **Make your changes** - Implement your feature or bug fix
5. **Test thoroughly** - Ensure all tests pass and add new tests if needed
6. **Commit your changes** - `git commit -m 'Add amazing feature'`
7. **Push to your fork** - `git push origin feature/amazing-feature`
8. **Open a Pull Request** - Submit your PR with a clear description

### Contribution Guidelines

- **Code Style**: Follow PEP 8 style guide for Python code
- **Testing**: Add tests for new features and ensure existing tests pass
- **Documentation**: Update README.md and relevant docs for new features
- **Commits**: Keep commits focused, atomic, and with descriptive messages
- **Pull Requests**: Provide clear description of changes and link related issues
- **Issues**: Check existing issues before creating new ones

### Areas for Contribution

- 🐛 Bug fixes and issue resolution
- ✨ New features and enhancements
- 📝 Documentation improvements
- 🧪 Test coverage expansion
- 🎨 UI/UX improvements
- 🌍 Internationalization (i18n)
- ⚡ Performance optimizations
- 🔒 Security enhancements

### Code of Conduct

Please be respectful and constructive in all interactions. We're here to learn and build together.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support & Help

Need help? We've got you covered:

### Documentation Resources

- 📖 **[PROJECT_GUIDE.md](PROJECT_GUIDE.md)** - Comprehensive technical documentation
- 🎓 **[training/guide.md](training/guide.md)** - Complete model training guide
- � **[CHANGELOG.md](CHANGELOG.md)** - Version history and updates
- 💡 **[API Reference](#-api-reference)** - API endpoints and usage examples

### Get Help

- � **Bug Reports**: [Open an issue](https://github.com/yourusername/movie-recommendation-system/issues) with detailed description
- 💬 **Questions**: [GitHub Discussions](https://github.com/yourusername/movie-recommendation-system/discussions) for Q&A
- 💡 **Feature Requests**: [Request a feature](https://github.com/yourusername/movie-recommendation-system/issues/new) with use case
- 🔧 **Troubleshooting**: Check [PROJECT_GUIDE.md - Troubleshooting](PROJECT_GUIDE.md#-troubleshooting)

### Common Issues

| Issue | Solution |
|-------|----------|
| Port 8000 already in use | Use `python manage.py runserver 8080` |
| Module not found | Run `pip install -r requirements.txt` |
| Model not loading | Check `MODEL_DIR` environment variable |
| Slow recommendations | Enable SVD dimensionality reduction |
| Memory errors | Reduce dataset size or increase RAM |

---

## 🎯 Roadmap

### 🚀 Version 2.1 (Q2 2026)
- [ ] User authentication and profiles
- [ ] Personal watchlists and favorites
- [ ] Movie rating and review system
- [ ] Advanced filtering (multiple genres, year ranges, ratings)
- [ ] Recommendation history and tracking
- [ ] Export recommendations to CSV/JSON
- [ ] Dark mode UI theme

### 🌟 Version 2.2 (Q3 2026)
- [ ] Collaborative filtering (user-based recommendations)
- [ ] Hybrid recommendation engine (content + collaborative)
- [ ] Social features (sharing, comments, follows)
- [ ] Movie reviews and user-generated content
- [ ] Advanced analytics dashboard
- [ ] A/B testing framework for recommendations
- [ ] Multi-language support (i18n)

### 🔮 Version 3.0 (Q4 2026 - Long-term)
- [ ] Mobile applications (iOS/Android native apps)
- [ ] Real-time recommendations with WebSocket
- [ ] Streaming service integration (Netflix, Prime, etc.)
- [ ] Enhanced ML models (deep learning, transformers)
- [ ] Recommendation explanations (why this movie?)
- [ ] Video trailers and clips integration
- [ ] GraphQL API support
- [ ] Microservices architecture

### 💡 Community Requested Features
- [ ] Batch recommendation API endpoint
- [ ] Movie comparison tool
- [ ] Recommendation diversity controls
- [ ] Custom recommendation algorithms
- [ ] Integration with Plex/Jellyfin
- [ ] Recommendation email notifications

Want to contribute to the roadmap? [Open a feature request](https://github.com/yourusername/movie-recommendation-system/issues/new)!

---

## 📊 Performance Benchmarks

Performance metrics tested on standard hardware (Intel i5, 16GB RAM):

| Metric | Demo (2K) | Medium (10K) | Large (100K) | Extra Large (1M) |
|--------|-----------|--------------|--------------|------------------|
| **Recommendation Time** | < 10ms | < 20ms | < 50ms | < 100ms |
| **Search Response** | < 50ms | < 75ms | < 100ms | < 150ms |
| **Page Load Time** | < 100ms | < 150ms | < 200ms | < 300ms |
| **Memory Usage** | ~50MB | ~100MB | ~200MB | ~1.5GB |
| **Model Load Time** | < 1s | < 3s | < 10s | < 30s |
| **Concurrent Users** | 500+ | 1000+ | 1000+ | 500+ |
| **Model Size (Disk)** | 5MB | 25MB | 180MB | 1.2GB |

### Optimization Tips

- Use SVD dimensionality reduction for datasets > 10K movies
- Enable Parquet compression for 5-10x storage savings
- Configure quality thresholds to filter low-quality movies
- Use caching for frequently accessed recommendations
- Deploy with Gunicorn/uWSGI for production workloads

---

## 🙏 Acknowledgments

This project wouldn't be possible without:

### Data Sources
- **[The Movie Database (TMDB)](https://www.themoviedb.org/)** - Movie metadata and information
- **[IMDb](https://www.imdb.com/)** - Movie ratings and additional data
- **[Kaggle](https://www.kaggle.com/)** - Movie datasets for training

### Technologies & Libraries
- **[Django](https://www.djangoproject.com/)** - Web framework
- **[scikit-learn](https://scikit-learn.org/)** - Machine learning algorithms
- **[pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[NumPy](https://numpy.org/)** - Numerical computing
- **[SciPy](https://scipy.org/)** - Scientific computing

### Inspiration & Resources
- Modern UI/UX design principles
- Content-based filtering research papers
- Open source community contributions
- Developer feedback and suggestions

### Special Thanks
- All contributors who have helped improve this project
- The open source community for amazing tools and libraries
- Movie enthusiasts who provided valuable feedback

---

## ⚖️ Legal & Compliance

### Data Usage
This project uses publicly available movie data for educational and non-commercial purposes. When deploying in production:
- Ensure compliance with TMDB and IMDb terms of service
- Respect data usage policies and attribution requirements
- Consider data licensing for commercial applications

### Privacy
- No personal data is collected by default
- User searches are not logged or stored
- See [Privacy Policy](PRIVACY.md) for details (if applicable)

---

## 📈 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/movie-recommendation-system?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/movie-recommendation-system?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/movie-recommendation-system)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/movie-recommendation-system)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/movie-recommendation-system)
![GitHub code size](https://img.shields.io/github/languages/code-size/yourusername/movie-recommendation-system)

---

<div align="center">

**Made with ❤️ for movie lovers and developers**

[⭐ Star this repo](https://github.com/yourusername/movie-recommendation-system) •
[🐛 Report Bug](https://github.com/yourusername/movie-recommendation-system/issues) •
[💡 Request Feature](https://github.com/yourusername/movie-recommendation-system/issues) •
[📖 Documentation](PROJECT_GUIDE.md)

---

### Show Your Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs and issues
- 💡 Suggesting new features
- 🤝 Contributing code or documentation
- 📢 Sharing with others who might find it useful

**Happy movie watching! 🍿**

</div>
