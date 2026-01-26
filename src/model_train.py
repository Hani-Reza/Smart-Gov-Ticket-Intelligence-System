"""
GCC Smart-Gov Ticket Intelligence System
Machine Learning Model Training Module
Author: Principal AI/ML Engineer
Production-grade model training with enterprise safeguards
"""

import pandas as pd
import numpy as np
import joblib
import logging
from datetime import datetime
from pathlib import Path
from typing import Tuple, Dict, Any

# ML imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ModelTrainer:
    """
    Production-grade model trainer for UAE government ticket classification.
    Implements separate models for category classification and sentiment analysis.
    """
    
    def __init__(self, data_path: str = "data/tickets_synthetic_v2.csv"):
        """
        Initialize the model trainer.
        
        Args:
            data_path: Path to the synthetic ticket data
        """
        self.data_path = data_path
        self.data = None
        self.category_model = None
        self.sentiment_model = None
        self.vectorizer = None
        self.models_dir = Path("../models")
        
        # Create models directory if it doesn't exist
        self.models_dir.mkdir(exist_ok=True)
        
        logger.info("ModelTrainer initialized for GCC Smart-Gov System")
    
    def load_data(self) -> pd.DataFrame:
        """Load and prepare the synthetic ticket data."""
        try:
            self.data = pd.read_csv(self.data_path)
            logger.info(f"Loaded {len(self.data)} tickets from {self.data_path}")
            
            # Basic data validation
            required_columns = ['text', 'category', 'sentiment']
            missing_cols = [col for col in required_columns if col not in self.data.columns]
            
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
            
            # Clean text data
            self.data['text_clean'] = self.data['text'].str.lower().str.strip()
            
            # Verify distribution
            logger.info("Data distribution:")
            logger.info(f"Categories: {self.data['category'].value_counts().to_dict()}")
            logger.info(f"Sentiments: {self.data['sentiment'].value_counts().to_dict()}")
            
            return self.data
            
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
    
    def create_ml_pipeline(self) -> Pipeline:
        """
        Create ML pipeline with TF-IDF vectorizer and Logistic Regression.
        
        Returns:
            Configured scikit-learn Pipeline
        """
        # TF-IDF Vectorizer with parameters optimized for ticket text
        vectorizer = TfidfVectorizer(
            max_features=5000,
            min_df=2,
            max_df=0.95,
            ngram_range=(1, 2),
            stop_words='english',
            sublinear_tf=True  # Use 1 + log(tf) instead of raw tf
        )
        
        # Logistic Regression with balanced class weights
        classifier = LogisticRegression(
            max_iter=1000,
            random_state=42,
            class_weight='balanced',
            solver='liblinear',  # Good for small to medium datasets
            C=1.0,
            penalty='l2'
        )
        
        # Create pipeline
        pipeline = Pipeline([
            ('vectorizer', vectorizer),
            ('classifier', classifier)
        ])
        
        return pipeline
    
    def train_category_model(self) -> Tuple[Pipeline, Dict[str, Any]]:
        """
        Train model for ticket category classification.
        
        Returns:
            Tuple of (trained_pipeline, metrics_dict)
        """
        logger.info("Training category classification model...")
        
        # Prepare data
        X = self.data['text_clean'].values
        y = self.data['category'].values
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Create and train pipeline
        pipeline = self.create_ml_pipeline()
        pipeline.fit(X_train, y_train)
        
        # Evaluate
        y_pred = pipeline.predict(X_test)
        y_pred_proba = pipeline.predict_proba(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        # Calculate confidence metrics
        avg_confidence = np.max(y_pred_proba, axis=1).mean()
        confidence_std = np.max(y_pred_proba, axis=1).std()
        
        metrics = {
            'accuracy': accuracy,
            'precision': report['weighted avg']['precision'],
            'recall': report['weighted avg']['recall'],
            'f1_score': report['weighted avg']['f1-score'],
            'avg_confidence': avg_confidence,
            'confidence_std': confidence_std,
            'test_samples': len(X_test),
            'training_date': datetime.now().isoformat()
        }
        
        logger.info(f"Category model accuracy: {accuracy:.3f}")
        logger.info(f"Average confidence: {avg_confidence:.3f} ± {confidence_std:.3f}")
        
        self.category_model = pipeline
        return pipeline, metrics
    
    def train_sentiment_model(self) -> Tuple[Pipeline, Dict[str, Any]]:
        """
        Train model for sentiment analysis.
        
        Returns:
            Tuple of (trained_pipeline, metrics_dict)
        """
        logger.info("Training sentiment analysis model...")
        
        # Prepare data
        X = self.data['text_clean'].values
        y = self.data['sentiment'].values
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Create and train pipeline
        pipeline = self.create_ml_pipeline()
        pipeline.fit(X_train, y_train)
        
        # Evaluate
        y_pred = pipeline.predict(X_test)
        y_pred_proba = pipeline.predict_proba(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        # Calculate confidence metrics
        avg_confidence = np.max(y_pred_proba, axis=1).mean()
        confidence_std = np.max(y_pred_proba, axis=1).std()
        
        metrics = {
            'accuracy': accuracy,
            'precision': report['weighted avg']['precision'],
            'recall': report['weighted avg']['recall'],
            'f1_score': report['weighted avg']['f1-score'],
            'avg_confidence': avg_confidence,
            'confidence_std': confidence_std,
            'test_samples': len(X_test),
            'training_date': datetime.now().isoformat()
        }
        
        logger.info(f"Sentiment model accuracy: {accuracy:.3f}")
        logger.info(f"Average confidence: {avg_confidence:.3f} ± {confidence_std:.3f}")
        
        self.sentiment_model = pipeline
        return pipeline, metrics
    
    def save_models(self):
        """Save trained models to disk."""
        if not self.category_model or not self.sentiment_model:
            logger.error("Models not trained yet. Call train methods first.")
            return False
        
        try:
            # Save category model
            category_path = self.models_dir / "category_model.pkl"
            joblib.dump(self.category_model, category_path)
            logger.info(f"Saved category model to {category_path}")
            
            # Save sentiment model
            sentiment_path = self.models_dir / "sentiment_model.pkl"
            joblib.dump(self.sentiment_model, sentiment_path)
            logger.info(f"Saved sentiment model to {sentiment_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error saving models: {e}")
            return False
    
    def train_all_models(self) -> Dict[str, Any]:
        """
        Train both category and sentiment models.
        
        Returns:
            Dictionary containing training metrics for both models
        """
        logger.info("Starting comprehensive model training...")
        
        # Load data
        self.load_data()
        
        # Train models
        category_pipeline, category_metrics = self.train_category_model()
        sentiment_pipeline, sentiment_metrics = self.train_sentiment_model()
        
        # Save models
        save_success = self.save_models()
        
        if save_success:
            logger.info("✅ All models trained and saved successfully!")
        else:
            logger.error("❌ Failed to save models")
        
        # Return comprehensive metrics
        return {
            'category_model': category_metrics,
            'sentiment_model': sentiment_metrics,
            'models_saved': save_success,
            'training_completed': datetime.now().isoformat()
        }


def validate_models():
    """Validate that saved models can be loaded and used."""
    try:
        # Load models
        category_model = joblib.load("../models/category_model.pkl")
        sentiment_model = joblib.load("../models/sentiment_model.pkl")
        
        # Test with sample text
        test_texts = [
            "DEWA bill is incorrect",
            "Fire alarm not working in building",
            "RTA website is very user friendly"
        ]
        
        print("🔍 Model Validation Results:")
        print("-" * 50)
        
        for text in test_texts:
            category = category_model.predict([text])[0]
            category_conf = category_model.predict_proba([text]).max()
            sentiment = sentiment_model.predict([text])[0]
            sentiment_conf = sentiment_model.predict_proba([text]).max()
            
            print(f"Text: '{text}'")
            print(f"  Category: {category} (confidence: {category_conf:.3f})")
            print(f"  Sentiment: {sentiment} (confidence: {sentiment_conf:.3f})")
            print()
        
        return True
        
    except Exception as e:
        print(f"❌ Model validation failed: {e}")
        return False


def main():
    """Main training execution function."""
    print("=" * 60)
    print("GCC SMART-GOV TICKET INTELLIGENCE SYSTEM")
    print("PRODUCTION MODEL TRAINING MODULE")
    print("=" * 60)
    
    try:
        # Initialize trainer
        trainer = ModelTrainer()
        
        # Train all models
        metrics = trainer.train_all_models()
        
        # Print summary
        print("\n📊 TRAINING SUMMARY")
        print("=" * 40)
        print("Category Model:")
        for key, value in metrics['category_model'].items():
            if isinstance(value, float):
                print(f"  {key}: {value:.3f}")
            else:
                print(f"  {key}: {value}")
        
        print("\nSentiment Model:")
        for key, value in metrics['sentiment_model'].items():
            if isinstance(value, float):
                print(f"  {key}: {value:.3f}")
            else:
                print(f"  {key}: {value}")
        
        # Validate models
        print("\n🔧 Model Validation:")
        if validate_models():
            print("✅ All models validated successfully!")
        else:
            print("❌ Model validation failed!")
        
        print("\n🎯 Training completed successfully!")
        
    except Exception as e:
        logger.error(f"Training failed: {e}")
        print(f"❌ Training failed: {e}")
        return False
    
    return True


if __name__ == "__main__":
    main()