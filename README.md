# Student Performance Prediction System (AI-Powered)

This project uses Machine Learning to predict student academic outcomes based on various demographic and academic factors.

## 🚀 Deployment

This project is optimized for deployment on **Vercel**.

### Prerequisites
- [Vercel CLI](https://vercel.com/download) installed
- [Git](https://git-scm.com/) installed

### Deployment Steps
1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```
2. **Deploy via Vercel**:
   - Run `npx vercel` in the root directory.
   - Link the project and follow the prompts.
   - Vercel will automatically detect the `vercel.json` and deploy both the FastAPI backend and Next.js frontend.

## 🛠️ Architecture
- **Backend**: FastAPI with Scikit-learn models (Logistic Regression, KNN, Decision Tree, Random Forest).
- **Frontend**: Next.js with Chart.js for interactive analytics.
- **Routing**: Optimized via `vercel.json` for serverless monorepo support.
