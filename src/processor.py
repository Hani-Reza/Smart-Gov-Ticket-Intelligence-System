"""
GCC Smart-Gov Ticket Intelligence System
Enterprise Processing Engine with UAE Safeguards - FIXED VERSION
Author: Principal AI/ML Engineer
Production-grade ticket processing with PII protection and safety overrides
"""

import re
import joblib
import logging
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path
import json

# Configure logging for audit trail
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('../logs/system_audit.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class PIIProtector:
    """
    UAE-specific PII detection and masking for Emirates ID and phone numbers.
    """
    
    EMIRATES_ID_PATTERN = r'\b784-\d{4}-\d{7}-\d\b'
    PHONE_PATTERNS = [
        r'\+\d{10,15}',
        r'\b05\d-\d{7}\b',
        r'\b05\d{8}\b',
        r'\b\+9715\d{8}\b'
    ]
    
    @staticmethod
    def mask_emirates_id(text: str) -> Tuple[str, List[str]]:
        detected_ids = re.findall(PIIProtector.EMIRATES_ID_PATTERN, text)
        masked_text = text
        
        for eid in detected_ids:
            parts = eid.split('-')
            if len(parts) == 4:
                masked_id = f"{parts[0]}-{parts[1]}-XXX-{parts[3]}"
                masked_text = masked_text.replace(eid, masked_id)
        
        return masked_text, detected_ids
    
    @staticmethod
    def mask_phone_numbers(text: str) -> Tuple[str, List[str]]:
        detected_numbers = []
        masked_text = text
        
        for pattern in PIIProtector.PHONE_PATTERNS:
            numbers = re.findall(pattern, text)
            detected_numbers.extend(numbers)
            
            for number in numbers:
                if number.startswith('+971'):
                    masked = f"+971-XXX-XXXX"
                elif number.startswith('05'):
                    masked = f"05X-XXX-XXXX"
                else:
                    masked = "XXX-XXX-XXXX"
                
                masked_text = masked_text.replace(number, masked)
        
        return masked_text, detected_numbers
    
    @staticmethod
    def mask_all_pii(text: str) -> Dict[str, Any]:
        masked_text, emirates_ids = PIIProtector.mask_emirates_id(text)
        masked_text, phone_numbers = PIIProtector.mask_phone_numbers(masked_text)
        
        return {
            'masked_text': masked_text,
            'original_text': text,
            'detected_emirates_ids': emirates_ids,
            'detected_phone_numbers': phone_numbers,
            'has_pii': len(emirates_ids) > 0 or len(phone_numbers) > 0
        }


class SafetyOverrideEngine:
    """
    Rule-based safety override engine for emergency situations.
    """
    
    SAFETY_KEYWORDS = {
        'fire': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'emergency': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'urgent': {'category': 'Safety / Emergency', 'priority': 'High', 'response_time': '1 hour'},
        'accident': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'trapped': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'gas leak': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'electrocution': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'collapse': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'explosion': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'ambulance': {'category': 'Safety / Emergency', 'priority': 'Critical', 'response_time': '15 minutes'},
        'police needed': {'category': 'Safety / Emergency', 'priority': 'High', 'response_time': '30 minutes'}
    }
    
    SPAM_THRESHOLD = 3
    
    @staticmethod
    def check_safety_override(text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        found_keywords = []
        spam_score = 0
        
        for keyword, override_info in SafetyOverrideEngine.SAFETY_KEYWORDS.items():
            if keyword in text_lower:
                found_keywords.append(keyword)
                spam_score += 1
        
        needs_override = len(found_keywords) > 0
        is_spam = spam_score > SafetyOverrideEngine.SPAM_THRESHOLD
        
        if needs_override and not is_spam:
            # Find most critical override
            override_info = None
            for keyword in found_keywords:
                if override_info is None or SafetyOverrideEngine.SAFETY_KEYWORDS[keyword]['priority'] == 'Critical':
                    override_info = SafetyOverrideEngine.SAFETY_KEYWORDS[keyword]
        
        return {
            'needs_override': needs_override,
            'is_spam': is_spam,
            'found_keywords': found_keywords,
            'override_category': override_info['category'] if needs_override and not is_spam else None,
            'override_priority': override_info['priority'] if needs_override and not is_spam else None,
            'response_time': override_info['response_time'] if needs_override and not is_spam else None,
            'spam_score': spam_score
        }


class TicketProcessor:
    """
    Main ticket processing engine with clear business outputs.
    """
    
    def __init__(self):
        self.category_model = None
        self.sentiment_model = None
        self.pii_protector = PIIProtector()
        self.safety_engine = SafetyOverrideEngine()
        self.confidence_threshold = 0.55
        self.load_models()
        logger.info("TicketProcessor initialized")
    
    def load_models(self):
        try:
            models_dir = Path("../models")
            
            category_path = models_dir / "category_model.pkl"
            if category_path.exists():
                self.category_model = joblib.load(category_path)
                logger.info("Category model loaded")
            
            sentiment_path = models_dir / "sentiment_model.pkl"
            if sentiment_path.exists():
                self.sentiment_model = joblib.load(sentiment_path)
                logger.info("Sentiment model loaded")
                
        except Exception as e:
            logger.error(f"Error loading models: {e}")
    
    def _get_clear_action_items(self, category: str, sentiment: str, priority: str) -> List[str]:
        """Generate clear action items for government staff."""
        actions = []
        
        if priority == 'Critical':
            actions.append("🆘 **IMMEDIATE ACTION REQUIRED**: Contact emergency services")
            actions.append("📞 Notify department head immediately")
            actions.append("⏰ Response time: 15 minutes maximum")
        
        if category == 'Safety / Emergency':
            actions.append("🚨 Activate emergency response protocol")
            actions.append("📍 Dispatch field team to location")
            actions.append("📋 Document incident for compliance")
        
        elif category == 'Technical / IT':
            actions.append("💻 Assign to IT support team")
            if priority == 'High':
                actions.append("⏰ SLA: Resolve within 4 hours")
            else:
                actions.append("⏰ SLA: Resolve within 24 hours")
        
        elif category == 'Billing':
            actions.append("💰 Forward to finance department")
            actions.append("📊 Verify charges with billing system")
            actions.append("✉️ Send acknowledgment email to citizen")
        
        elif category == 'Facilities':
            actions.append("🔧 Assign maintenance team")
            if priority == 'High':
                actions.append("⏰ SLA: Address within 8 hours")
            else:
                actions.append("⏰ SLA: Address within 48 hours")
        
        elif category == 'Inquiry':
            actions.append("📞 Contact citizen for clarification")
            actions.append("📚 Provide information package")
            actions.append("⏰ SLA: Respond within 24 hours")
        
        if sentiment == 'Negative':
            actions.append("😠 **Citizen frustration detected**: Escalate to supervisor")
            actions.append("📞 Call citizen to address concerns")
        
        elif sentiment == 'Positive':
            actions.append("✅ **Positive feedback**: Log for employee recognition")
        
        return actions
    
    def _get_department_contact(self, department: str) -> Dict[str, str]:
        """Get department contact information."""
        contacts = {
            'Emergency Response Center': {
                'phone': '999',
                'email': 'emergency@uae.gov.ae',
                'supervisor': 'Col. Ahmed Al Mansoori'
            },
            'IT Support Division': {
                'phone': '800-IT-HELP',
                'email': 'itsupport@uae.gov.ae',
                'supervisor': 'Eng. Fatima Al Zahrani'
            },
            'Finance & Accounts Department': {
                'phone': '800-FINANCE',
                'email': 'finance@uae.gov.ae',
                'supervisor': 'Mr. Khalid Al Qasimi'
            },
            'Municipal Services Department': {
                'phone': '800-MUNICIPAL',
                'email': 'municipal@uae.gov.ae',
                'supervisor': 'Eng. Mohammed Al Shamsi'
            },
            'Customer Service Center': {
                'phone': '800-GOVERNMENT',
                'email': 'customerservice@uae.gov.ae',
                'supervisor': 'Ms. Sara Al Muhairi'
            },
            'Priority Escalation Team': {
                'phone': '800-PRIORITY',
                'email': 'escalation@uae.gov.ae',
                'supervisor': 'Director General Office'
            }
        }
        return contacts.get(department, {
            'phone': '800-GOVERNMENT',
            'email': 'info@uae.gov.ae',
            'supervisor': 'Department Head'
        })
    
    def process_text(self, text: str) -> Dict[str, Any]:
        start_time = datetime.now()
        
        # Step 1: PII Detection
        pii_result = self.pii_protector.mask_all_pii(text)
        processed_text = pii_result['masked_text']
        
        # Step 2: Safety Check
        safety_result = self.safety_engine.check_safety_override(processed_text)
        
        # Step 3: ML Predictions
        ml_results = {}
        if self.category_model and self.sentiment_model:
            category_pred = self.category_model.predict([processed_text])[0]
            category_proba = self.category_model.predict_proba([processed_text])
            category_confidence = float(category_proba.max())
            
            sentiment_pred = self.sentiment_model.predict([processed_text])[0]
            sentiment_proba = self.sentiment_model.predict_proba([processed_text])
            sentiment_confidence = float(sentiment_proba.max())
            
            ml_results = {
                'category': category_pred,
                'category_confidence': category_confidence,
                'sentiment': sentiment_pred,
                'sentiment_confidence': sentiment_confidence,
                'category_probabilities': dict(zip(
                    self.category_model.named_steps['classifier'].classes_,
                    category_proba[0]
                )),
                'sentiment_probabilities': dict(zip(
                    self.sentiment_model.named_steps['classifier'].classes_,
                    sentiment_proba[0]
                ))
            }
        else:
            ml_results = {
                'category': 'Unknown',
                'category_confidence': 0.0,
                'sentiment': 'Neutral',
                'sentiment_confidence': 0.0
            }
        
        # Step 4: Apply Safety Override
        if safety_result['needs_override'] and not safety_result['is_spam']:
            final_category = safety_result['override_category']
            final_priority = safety_result['override_priority']
            response_time = safety_result['response_time']
            override_applied = True
        else:
            final_category = ml_results['category']
            final_priority = self._determine_priority(final_category, ml_results['sentiment'])
            response_time = self._get_response_time(final_priority)
            override_applied = False
        
        # Step 5: Confidence Check
        min_confidence = min(ml_results['category_confidence'], ml_results['sentiment_confidence'])
        needs_manual_review = min_confidence < self.confidence_threshold or safety_result['is_spam']
        
        # Step 6: Department Routing
        department = self._route_to_department(final_category, ml_results['sentiment'])
        department_contact = self._get_department_contact(department)
        
        # Step 7: Action Items
        action_items = self._get_clear_action_items(final_category, ml_results['sentiment'], final_priority)
        
        # Step 8: Compile Results
        processing_time = (datetime.now() - start_time).total_seconds()
        
        results = {
            'ticket_processing': {
                'original_text': text,
                'processed_text': processed_text,
                'processing_time_seconds': processing_time,
                'timestamp': datetime.now().isoformat()
            },
            'pii_protection': pii_result,
            'safety_check': safety_result,
            'ml_predictions': ml_results,
            'final_decisions': {
                'category': final_category,
                'sentiment': ml_results['sentiment'],
                'priority': final_priority,
                'department': department,
                'department_contact': department_contact,
                'response_time': response_time,
                'confidence_score': min_confidence,
                'needs_manual_review': needs_manual_review,
                'manual_review_reason': 'Low confidence' if min_confidence < self.confidence_threshold else 'Potential spam' if safety_result['is_spam'] else None,
                'safety_override_applied': override_applied,
                'action_items': action_items,
                'ticket_id': f"TKT-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{hash(text) % 10000:04d}"
            }
        }
        
        # Step 9: Audit Logging
        self._audit_log(results)
        
        return results
    
    def _determine_priority(self, category: str, sentiment: str) -> str:
        priority_rules = {
            'Safety / Emergency': 'Critical' if sentiment == 'Negative' else 'High',
            'Technical / IT': 'High' if sentiment == 'Negative' else 'Medium',
            'Billing': 'High' if sentiment == 'Negative' else 'Medium',
            'Facilities': 'High' if sentiment == 'Negative' else 'Medium',
            'Inquiry': 'Medium' if sentiment == 'Negative' else 'Low'
        }
        return priority_rules.get(category, 'Medium')
    
    def _get_response_time(self, priority: str) -> str:
        response_times = {
            'Critical': '15 minutes',
            'High': '1 hour',
            'Medium': '4 hours',
            'Low': '24 hours'
        }
        return response_times.get(priority, '4 hours')
    
    def _route_to_department(self, category: str, sentiment: str) -> str:
        routing_map = {
            'Safety / Emergency': 'Emergency Response Center',
            'Technical / IT': 'IT Support Division',
            'Billing': 'Finance & Accounts Department',
            'Facilities': 'Municipal Services Department',
            'Inquiry': 'Customer Service Center'
        }
        
        if sentiment == 'Negative' and category in ['Safety / Emergency', 'Technical / IT']:
            return 'Priority Escalation Team'
        
        return routing_map.get(category, 'Customer Service Center')
    
    def _audit_log(self, results: Dict[str, Any]):
        try:
            audit_entry = {
                'timestamp': results['ticket_processing']['timestamp'],
                'ticket_id': results['final_decisions']['ticket_id'],
                'category': results['final_decisions']['category'],
                'priority': results['final_decisions']['priority'],
                'department': results['final_decisions']['department'],
                'confidence': results['final_decisions']['confidence_score'],
                'manual_review': results['final_decisions']['needs_manual_review'],
                'processing_time': results['ticket_processing']['processing_time_seconds']
            }
            
            log_file = Path("../logs/system_audit.log")
            with open(log_file, 'a') as f:
                f.write(json.dumps(audit_entry) + '\n')
            
        except Exception as e:
            logger.error(f"Error writing audit log: {e}")