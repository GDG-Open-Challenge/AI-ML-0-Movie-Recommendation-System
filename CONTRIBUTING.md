# Contributing to Movie Recommendation System

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

---

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, background, or identity.

### Expected Behavior

- Be respectful and considerate
- Use welcoming and inclusive language
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other contributors

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling or insulting/derogatory comments
- Publishing others' private information
- Any conduct that could be considered inappropriate in a professional setting

---

## 🚀 Getting Started

### Prerequisites

Before contributing, ensure you have:

- Python 3.11 or higher
- Git installed and configured
- Basic understanding of Django and Python
- Familiarity with machine learning concepts (for ML-related contributions)

### Finding Issues to Work On

1. Check the [Issues](https://github.com/yourusername/movie-recommendation-system/issues) page
2. Look for issues labeled:
   - `good first issue` - Great for newcomers
   - `help wanted` - We need assistance
   - `bug` - Something isn't working
   - `enhancement` - New feature or improvement

3. Comment on the issue to let others know you're working on it

---

## 💻 Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git
cd movie-recommendation-system

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/movie-recommendation-system.git
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install all dependencies
pip install -r requirements.txt

# Install development dependencies (if available)
# pip install -r requirements-dev.txt
```

### 4. Set Up Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings
# At minimum, set SECRET_KEY and DEBUG=True
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Verify Setup

```bash
# Run tests
python manage.py test

# Start development server
python manage.py runserver

# Visit http://localhost:8000
```

---

## 🔧 How to Contribute

### 1. Create a Branch

```bash
# Update your main branch
git checkout main
git pull upstream main

# Create a feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-description
```

### Branch Naming Convention

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Adding or updating tests
- `chore/` - Maintenance tasks

### 2. Make Your Changes

- Write clean, readable code
- Follow the coding standards (see below)
- Add tests for new functionality
- Update documentation as needed
- Keep commits focused and atomic

### 3. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add feature: brief description"
```

#### Commit Message Guidelines

Format: `<type>: <subject>`

Types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

Examples:
```
feat: Add user authentication system
fix: Resolve memory leak in model loading
docs: Update installation instructions
test: Add tests for recommendation API
```

### 4. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Go to GitHub and create a Pull Request
```

---

## 📝 Coding Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line Length**: Maximum 100 characters (not 79)
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Use single quotes for strings unless double quotes avoid escaping

### Code Formatting

```bash
# Install formatters
pip install black flake8 isort

# Format code
black .

# Sort imports
isort .

# Check for issues
flake8 .
```

### Django Best Practices

1. **Views**
   - Keep views thin, move logic to models or services
   - Use class-based views for complex logic
   - Add docstrings to all views

2. **Models**
   - Add `__str__` methods
   - Use `help_text` for fields
   - Add database indexes where appropriate

3. **Templates**
   - Use template inheritance
   - Keep logic minimal in templates
   - Use template tags for reusable components

4. **URLs**
   - Use meaningful URL names
   - Use path() instead of url()
   - Group related URLs

### Documentation

- Add docstrings to all functions, classes, and modules
- Use Google-style docstrings
- Update README.md for user-facing changes
- Update PROJECT_GUIDE.md for technical changes

Example:
```python
def get_recommendations(movie_title: str, n: int = 15) -> Dict:
    """
    Get movie recommendations based on similarity.
    
    Args:
        movie_title: Title of the movie to base recommendations on
        n: Number of recommendations to return (default: 15)
    
    Returns:
        Dictionary containing recommendations and metadata
        
    Raises:
        MovieNotFoundError: If the movie title is not found
    """
    # Implementation
```

---

## 🧪 Testing Guidelines

### Writing Tests

1. **Test Coverage**
   - Aim for 80%+ code coverage
   - Test all new features
   - Test edge cases and error conditions

2. **Test Organization**
   ```python
   # recommender/tests.py
   class FeatureTests(TestCase):
       def setUp(self):
           # Setup code
           pass
       
       def test_specific_behavior(self):
           # Test code
           pass
   ```

3. **Test Naming**
   - Use descriptive names: `test_user_can_search_movies`
   - Not: `test1`, `test_search`

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test recommender

# Run specific test class
python manage.py test recommender.tests.RecommendationTests

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Test Requirements

- All new features must have tests
- Bug fixes should include regression tests
- Tests must pass before PR is merged
- Maintain or improve code coverage

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update your branch**
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-branch
   git rebase main
   ```

2. **Run tests**
   ```bash
   python manage.py test
   ```

3. **Check code quality**
   ```bash
   black .
   flake8 .
   ```

4. **Update documentation**
   - Update README.md if needed
   - Add docstrings to new code
   - Update CHANGELOG.md

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Updated existing tests

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] All tests pass

## Screenshots (if applicable)
Add screenshots for UI changes

## Related Issues
Closes #123
```

### Review Process

1. **Automated Checks**
   - Tests must pass
   - Code quality checks must pass
   - No merge conflicts

2. **Code Review**
   - At least one approval required
   - Address all review comments
   - Make requested changes

3. **Merge**
   - Maintainer will merge when approved
   - Branch will be deleted after merge

---

## 🐛 Reporting Bugs

### Before Reporting

1. Check if the bug has already been reported
2. Try to reproduce the bug
3. Gather relevant information

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 10, macOS 12]
- Python version: [e.g., 3.11]
- Django version: [e.g., 6.0]
- Browser: [e.g., Chrome 120]

**Additional context**
Any other relevant information.
```

---

## 💡 Suggesting Features

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Other solutions or features you've considered.

**Additional context**
Any other context, mockups, or examples.

**Would you like to implement this feature?**
- [ ] Yes, I'd like to implement it
- [ ] No, just suggesting
```

---

## 📚 Additional Resources

### Documentation

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Git Workflow](https://guides.github.com/introduction/flow/)

### Learning Resources

- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Python Testing](https://realpython.com/python-testing/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

### Communication

- GitHub Issues - Bug reports and feature requests
- GitHub Discussions - Questions and general discussion
- Pull Requests - Code review and discussion

---

## 🙏 Thank You!

Thank you for contributing to the Movie Recommendation System! Your efforts help make this project better for everyone.

### Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in the project

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

**Questions?** Feel free to ask in [GitHub Discussions](https://github.com/yourusername/movie-recommendation-system/discussions) or open an issue.
