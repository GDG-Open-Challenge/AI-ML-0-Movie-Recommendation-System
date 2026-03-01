"""
Custom exceptions for the Movie Recommendation System
"""


class RecommenderException(Exception):
    """Base exception for recommender system"""
    pass


class ModelNotLoadedError(RecommenderException):
    """Raised when model is not loaded or still loading"""
    def __init__(self, message="Model is not loaded yet. Please wait for model to finish loading."):
        self.message = message
        super().__init__(self.message)


class MovieNotFoundError(RecommenderException):
    """Raised when a movie is not found in the database"""
    def __init__(self, movie_title, suggestions=None):
        self.movie_title = movie_title
        self.suggestions = suggestions or []
        self.message = f"Movie '{movie_title}' not found in database"
        super().__init__(self.message)


class InvalidModelDirectoryError(RecommenderException):
    """Raised when model directory is invalid or missing required files"""
    def __init__(self, model_dir, missing_files=None):
        self.model_dir = model_dir
        self.missing_files = missing_files or []
        if missing_files:
            self.message = f"Model directory '{model_dir}' is missing required files: {', '.join(missing_files)}"
        else:
            self.message = f"Model directory '{model_dir}' is invalid or does not exist"
        super().__init__(self.message)


class ModelLoadError(RecommenderException):
    """Raised when model fails to load"""
    def __init__(self, message="Failed to load recommendation model", original_exception=None):
        self.message = message
        self.original_exception = original_exception
        if original_exception:
            self.message += f": {str(original_exception)}"
        super().__init__(self.message)


class RecommendationError(RecommenderException):
    """Raised when recommendation generation fails"""
    def __init__(self, message="Failed to generate recommendations"):
        self.message = message
        super().__init__(self.message)


class RateLimitExceededError(RecommenderException):
    """Raised when rate limit is exceeded"""
    def __init__(self, message="Rate limit exceeded. Please try again later."):
        self.message = message
        super().__init__(self.message)
