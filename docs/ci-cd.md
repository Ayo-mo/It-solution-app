# CI/CD Staging → Production Approval Flow

## Overview

The project uses separate GitHub Actions workflows for Staging and Production.

The deployment flow is:

**Code Push → Staging Build/Test → Docker Image → Docker Hub → Staging Deployment → Manual Production Approval → Production Deployment**

This setup demonstrates a basic CI/CD promotion process where Production deployment requires human approval.

---

## 1. Staging Workflow

The Staging workflow is:

`.github/workflows/ci-cd-staging.yml`

It is triggered by:

* Pushes to `main`
* Pushes to `feature/**`
* Pull requests targeting `main`

For a push to `main`, the workflow performs:

1. Checkout the repository.
2. Set up Python 3.10.
3. Install Python dependencies.
4. Check Python syntax with `py_compile`.
5. Build the Docker image.
6. Log in to Docker Hub.
7. Build and push the application image.
8. Deploy the application to the EC2 server.

The Docker image is pushed as:

```text
ayodeji2309/it-solution-app:latest
```

and also receives a Git SHA tag.

The Staging deployment uses the GitHub `Staging` environment.

---

## 2. Production Workflow

The Production workflow is:

`.github/workflows/ci-cd-production.yml`

Unlike Staging, Production is **not automatically triggered by a push**.

It uses:

```yaml
on:
  workflow_dispatch:
```

This means a Production deployment must be started manually from GitHub Actions.

The Production deployment uses the GitHub `Production` environment.

---

## 3. Production Approval Gate

The `Production` GitHub Environment has a **Required reviewer** configured.

The following protection settings were configured for the learning/test environment:

* Required reviewer: configured
* Prevent self-review: disabled
* Allow administrators to bypass protection rules: disabled

The workflow contains:

```yaml
environment:
  name: Production
```

Because the Production environment has a required reviewer, GitHub pauses the deployment before executing the deployment job.

GitHub displays a review request similar to:

> Ayo-mo requested your review to deploy to production.

The deployment remains paused until the required reviewer approves it.

---

## 4. Successful Approval Test

The Production workflow was manually started after the Staging workflow completed successfully.

GitHub correctly paused the deployment and displayed the Production deployment review.

The deployment was then approved manually.

Result:

```text
deploy-to-production: SUCCESS
```

This confirmed that the GitHub Environment protection rule is working correctly.

---

## 5. Current Deployment Architecture

The current flow is:

```text
Developer
   │
   │ git push
   ▼
GitHub
   │
   ▼
Staging Workflow
   │
   ├── Build & Test
   │
   ├── Build Docker Image
   │
   ├── Push Image to Docker Hub
   │
   └── Deploy to EC2
   │
   ▼
Staging Deployment
   │
   │ Manual Production Workflow
   ▼
Production Environment
   │
   │ Required Reviewer
   ▼
Manual Approval
   │
   ▼
Production Deployment
   │
   ▼
AWS EC2
```

---

## 6. Important Current Limitation

The current Staging and Production environments use the **same EC2 infrastructure**.

Therefore, the GitHub Environment names provide deployment controls and approval protection, but they do not currently represent two physically separate servers.

In addition, the Production workflow currently pulls:

```bash
docker compose pull
```

which retrieves the `latest` image.

Therefore, the current implementation demonstrates the **approval and promotion process**, but it does not yet guarantee that Production is deploying the exact immutable Docker image that was tested in Staging.

---

## 7. Next CI/CD Improvement

The next improvement should be:

**Build Once → Test → Deploy to Staging → Approve → Deploy the Exact Same Image to Production**

Instead of Production independently pulling:

```text
latest
```

Production should deploy the exact Docker image identified by its immutable Git SHA tag.

This will make the pipeline more reliable and bring it closer to a proper artifact-promotion model.

---

## Milestone Status

| Component                                  | Status               |
| ------------------------------------------ | -------------------- |
| GitHub Actions                             | ✅ Working            |
| Automated Staging workflow                 | ✅ Working            |
| Docker image build                         | ✅ Working            |
| Docker Hub push                            | ✅ Working            |
| EC2 deployment                             | ✅ Working            |
| Separate Production workflow               | ✅ Working            |
| Production environment                     | ✅ Configured         |
| Required reviewer                          | ✅ Configured         |
| Manual Production approval                 | ✅ Tested             |
| Production deployment                      | ✅ Successful         |
| Immutable artifact promotion               | ⏳ Next improvement   |
| Separate Staging/Production infrastructure | ⏳ Future improvement |
