# 🚀 Deployment Checklist

Use this checklist before deploying to production.

---

## ✅ Pre-Deployment Checklist

### 1. Environment Configuration

- [ ] Copy `.env.example` to `.env`
- [ ] Generate and set `SECRET_KEY`
  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Set `MODEL_DIR` to correct path
- [ ] Configure database URL (if using PostgreSQL)
- [ ] Set up Redis URL (if using Redis cache)

### 2. Dependencies

- [ ] Install all requirements
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Verify Python version (3.11+)
- [ ] Check for security updates
  ```bash
  pip list --outdated
  ```

### 3. Database

- [ ] Run migrations
  ```bash
  python manage.py migrate
  ```
- [ ] Create database backups
- [ ] Set up automated backup schedule
- [ ] Test database connection

### 4. Static Files

- [ ] Collect static files
  ```bash
  python manage.py collectstatic --noinput
  ```
- [ ] Verify static files are accessible
- [ ] Configure CDN (optional)

### 5. Testing

- [ ] Run all tests
  ```bash
  python manage.py test
  ```
- [ ] All tests pass
- [ ] Check test coverage
  ```bash
  coverage run --source='.' manage.py test
  coverage report
  ```
- [ ] Manual testing of critical features

### 6. Security

- [ ] SECRET_KEY is set and secure
- [ ] DEBUG is False
- [ ] ALLOWED_HOSTS is configured
- [ ] HTTPS is enabled
- [ ] CSRF protection enabled
- [ ] Rate limiting configured
- [ ] Security headers configured
- [ ] Run security check
  ```bash
  python manage.py check --deploy
  ```

### 7. Performance

- [ ] Caching is configured
- [ ] Database indexes are set
- [ ] Static files are compressed
- [ ] Gunicorn/uWSGI configured
- [ ] Worker count optimized
- [ ] Timeout settings configured

### 8. Monitoring

- [ ] Logging is configured
- [ ] Error tracking set up (Sentry, etc.)
- [ ] Health check endpoint works
- [ ] Monitoring dashboard configured
- [ ] Alerts configured

### 9. Documentation

- [ ] README.md is up to date
- [ ] API documentation is current
- [ ] Deployment guide is accurate
- [ ] Environment variables documented

### 10. Backup & Recovery

- [ ] Database backup strategy
- [ ] Model files backed up
- [ ] Recovery procedure documented
- [ ] Backup restoration tested

---

## 🐳 Docker Deployment

### Using Docker Compose

- [ ] Review `docker-compose.yml`
- [ ] Set environment variables
- [ ] Build images
  ```bash
  docker-compose build
  ```
- [ ] Start services
  ```bash
  docker-compose up -d
  ```
- [ ] Check logs
  ```bash
  docker-compose logs -f
  ```
- [ ] Verify health
  ```bash
  curl http://localhost:8000/api/health/
  ```

### Using Docker

- [ ] Build image
  ```bash
  docker build -t movie-recommender .
  ```
- [ ] Test locally
  ```bash
  docker run -p 8000:8000 -e SECRET_KEY=test movie-recommender
  ```
- [ ] Push to registry
  ```bash
  docker tag movie-recommender your-registry/movie-recommender
  docker push your-registry/movie-recommender
  ```

---

## ☁️ Platform-Specific Deployment

### Render

- [ ] Connect GitHub repository
- [ ] Configure build command
  ```
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```
- [ ] Configure start command
  ```
  gunicorn movie_recommendation.wsgi:application
  ```
- [ ] Set environment variables
- [ ] Configure health check path: `/api/health/`
- [ ] Deploy and verify

### Heroku

- [ ] Install Heroku CLI
- [ ] Create Heroku app
  ```bash
  heroku create your-app-name
  ```
- [ ] Add PostgreSQL
  ```bash
  heroku addons:create heroku-postgresql:mini
  ```
- [ ] Set environment variables
  ```bash
  heroku config:set SECRET_KEY="your-key"
  heroku config:set DEBUG=False
  ```
- [ ] Deploy
  ```bash
  git push heroku main
  ```
- [ ] Run migrations
  ```bash
  heroku run python manage.py migrate
  ```
- [ ] Open app
  ```bash
  heroku open
  ```

### AWS

- [ ] Install AWS CLI and EB CLI
- [ ] Initialize Elastic Beanstalk
  ```bash
  eb init -p python-3.11 movie-recommender
  ```
- [ ] Create environment
  ```bash
  eb create movie-recommender-env
  ```
- [ ] Set environment variables
- [ ] Deploy
  ```bash
  eb deploy
  ```
- [ ] Open app
  ```bash
  eb open
  ```

---

## 🔍 Post-Deployment Verification

### Functional Testing

- [ ] Home page loads
- [ ] Search functionality works
- [ ] Recommendations display correctly
- [ ] API endpoints respond
- [ ] Error pages display properly

### Performance Testing

- [ ] Response times acceptable
- [ ] Memory usage normal
- [ ] CPU usage normal
- [ ] Database queries optimized
- [ ] Caching working

### Security Testing

- [ ] HTTPS working
- [ ] Rate limiting active
- [ ] CSRF protection working
- [ ] XSS protection working
- [ ] Security headers present

### Monitoring

- [ ] Logs are being generated
- [ ] Errors are being tracked
- [ ] Metrics are being collected
- [ ] Alerts are configured
- [ ] Health check responding

---

## 🚨 Rollback Plan

If deployment fails:

1. **Immediate Actions**
   - [ ] Stop new deployments
   - [ ] Assess impact
   - [ ] Notify team

2. **Rollback Steps**
   - [ ] Revert to previous version
   - [ ] Restore database (if needed)
   - [ ] Clear cache
   - [ ] Verify rollback successful

3. **Post-Rollback**
   - [ ] Document what went wrong
   - [ ] Fix issues
   - [ ] Test fixes
   - [ ] Plan re-deployment

---

## 📊 Monitoring Checklist

### Daily

- [ ] Check error logs
- [ ] Review performance metrics
- [ ] Monitor resource usage
- [ ] Check backup status

### Weekly

- [ ] Review security logs
- [ ] Check for updates
- [ ] Review user feedback
- [ ] Analyze usage patterns

### Monthly

- [ ] Security audit
- [ ] Performance review
- [ ] Dependency updates
- [ ] Backup restoration test

---

## 🔧 Maintenance Tasks

### Regular Updates

- [ ] Update Python packages
  ```bash
  pip list --outdated
  pip install --upgrade package-name
  ```
- [ ] Update Django
- [ ] Update dependencies
- [ ] Test after updates

### Database Maintenance

- [ ] Vacuum database (PostgreSQL)
- [ ] Analyze query performance
- [ ] Review indexes
- [ ] Clean old data

### Cache Maintenance

- [ ] Clear old cache entries
- [ ] Review cache hit rates
- [ ] Optimize cache keys
- [ ] Monitor cache size

---

## 📞 Emergency Contacts

Document your emergency contacts:

- **DevOps Lead:** [Name, Contact]
- **Database Admin:** [Name, Contact]
- **Security Team:** [Name, Contact]
- **On-Call Engineer:** [Name, Contact]

---

## 📝 Deployment Log

Keep a record of deployments:

| Date | Version | Deployed By | Status | Notes |
|------|---------|-------------|--------|-------|
| 2026-03-01 | 2.0 | [Name] | ✅ Success | Initial production deployment |
| | | | | |

---

## ✅ Final Checklist

Before going live:

- [ ] All pre-deployment checks complete
- [ ] All tests passing
- [ ] Security audit passed
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] Team notified
- [ ] Monitoring configured
- [ ] Rollback plan ready
- [ ] Emergency contacts documented

---

**🎉 Ready to Deploy!**

Once all items are checked, you're ready for production deployment.

**Good luck! 🚀**
