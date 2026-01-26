"""
UAE Government AI Ticket Triage System
Production-Grade Streamlit Application - Fully Fixed Version
Senior Full-Stack AI Engineer - Enterprise Ready
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time
import sys
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple
import warnings
warnings.filterwarnings('ignore')

# Add src directory to path for imports
src_path = Path(__file__).parent
sys.path.append(str(src_path))

# Import our processor
try:
    from processor import TicketProcessor
    processor = TicketProcessor()
    MODELS_LOADED = processor.category_model is not None and processor.sentiment_model is not None
except ImportError as e:
    st.error(f"❌ System initialization failed: {str(e)}")
    MODELS_LOADED = False
except Exception as e:
    st.error(f"❌ Processor initialization failed: {str(e)}")
    MODELS_LOADED = False

# ============================================
# COMPLETE TRANSLATION SYSTEM WITH FIXED t() METHOD
# ============================================
class UAEGovernmentTranslator:
    """Complete bilingual translation system for UAE Government."""
    
    TRANSLATIONS = {
        "en": {
            # Application
            "app_title": "UAE Government AI Ticket Triage System",
            "app_subtitle": "Ministry of Artificial Intelligence • Secure Platform",
            
            # Navigation
            "tab_analyze": "📝 Ticket Analysis",
            "tab_history": "📚 Ticket History",
            
            # Sidebar
            "sidebar_system": "System Controls",
            "sidebar_language": "Language Selection",
            "sidebar_threshold": "Confidence Threshold",
            "sidebar_threshold_help": "Minimum confidence for automatic processing",
            "sidebar_user_role": "User Role",
            "sidebar_analyst": "Analyst",
            "sidebar_supervisor": "Supervisor",
            "sidebar_admin": "Administrator",
            "sidebar_stats": "System Statistics",
            "sidebar_processed": "Tickets Processed",
            "sidebar_accuracy": "Average Confidence",
            "sidebar_actions": "System Actions",
            "sidebar_clear": "🔄 Clear History",
            "sidebar_view_logs": "📊 View Audit Logs",
            "sidebar_status": "System Status",
            "sidebar_ai_models": "AI Models",
            "sidebar_security": "Security",
            "sidebar_pii": "PII Protection",
            "sidebar_audit": "Audit Logging",
            
            # Ticket Input
            "section_examples": "Example Tickets",
            "section_input": "Enter Ticket Details",
            "example_select": "Select an example ticket:",
            "input_label": "Ticket Text",
            "input_placeholder": "Enter detailed ticket description...",
            "btn_analyze": "🔍 Analyze Ticket",
            "btn_clear": "🧹 Clear Input",
            "input_stats": "Characters: {} | Words: {}",
            
            # Example Tickets
            "example_emergency": "🚨 Emergency Case",
            "example_emergency_desc": "Critical safety issue requiring immediate attention",
            "example_technical": "💻 Technical Issue",
            "example_technical_desc": "Government portal technical issue",
            "example_billing": "💰 Billing Problem",
            "example_billing_desc": "Citizen billing discrepancy investigation",
            "example_facilities": "🏢 Facilities Request",
            "example_facilities_desc": "Government building maintenance request",
            "example_inquiry": "📋 Service Inquiry",
            "example_inquiry_desc": "Citizen service request for documents",
            
            # Analysis Results
            "results_title": "Ticket Analysis Results",
            "results_ticket_id": "Ticket ID",
            "results_priority": "Priority Level",
            "results_response_time": "Response Time",
            "results_department": "Department",
            "results_confidence": "AI Confidence",
            "results_confidence_high": "High Confidence",
            "results_confidence_medium": "Medium Confidence",
            "results_confidence_low": "Low Confidence",
            "results_sentiment": "Citizen Sentiment",
            "results_category": "Category",
            "results_manual_review": "Manual Review Required",
            "results_auto_processing": "Auto-Processing Approved",
            "results_dissatisfaction": "Citizen Dissatisfaction Detected",
            "results_positive_feedback": "Positive Feedback Received",
            
            # Department
            "dept_assignment": "Department Assignment",
            "dept_supervisor": "Supervisor",
            "dept_contact": "Contact Information",
            "dept_phone": "Phone",
            "dept_email": "Email",
            "dept_action_required": "Action Required",
            
            # Actions
            "actions_title": "Required Actions",
            "action_emergency": "🚨 Activate emergency response protocol",
            "action_technical": "💻 Assign to IT support team",
            "action_billing": "💰 Forward to finance department",
            "action_facilities": "🔧 Assign maintenance team",
            "action_inquiry": "📞 Contact citizen for clarification",
            "action_standard": "Standard processing queue",
            
            # History Table
            "history_title": "Ticket History",
            "history_time": "Time",
            "history_ticket_id": "Ticket ID",
            "history_category": "Category",
            "history_priority": "Priority",
            "history_status": "Status",
            "history_ai_action": "AI Suggested Action",
            "history_no_data": "No ticket history available",
            "history_summary": "History Summary",
            "history_total": "Total Tickets",
            "history_avg_conf": "Average Confidence",
            "history_critical": "Critical Cases",
            "history_manual": "Manual Reviews",
            
            # Status Messages
            "status_processing": "Analyzing ticket with AI models...",
            "status_complete": "Analysis complete!",
            "status_error_empty": "Please enter ticket text",
            "status_error_models": "AI models not loaded. Please train models first.",
            "status_success": "Ticket processed successfully",
            
            # Footer
            "footer_title": "UAE Ministry of Artificial Intelligence",
            "footer_subtitle": "Smart Government Initiative • Secure Production",
            "footer_copyright": "© 2024 United Arab Emirates Government",
        },
        
        "ar": {
            # Application
            "app_title": "نظام تصنيف التذاكر الحكومي بالذكاء الاصطناعي",
            "app_subtitle": "وزارة الذكاء الاصطناعي • منصة آمنة",
            
            # Navigation
            "tab_analyze": "📝 تحليل التذاكر",
            "tab_history": "📚 سجل التذاكر",
            
            # Sidebar
            "sidebar_system": "عناصر تحكم النظام",
            "sidebar_language": "اختيار اللغة",
            "sidebar_threshold": "حد الثقة",
            "sidebar_threshold_help": "الحد الأدنى للثقة للمعالجة التلقائية",
            "sidebar_user_role": "دور المستخدم",
            "sidebar_analyst": "محلل",
            "sidebar_supervisor": "مشرف",
            "sidebar_admin": "مسؤول",
            "sidebar_stats": "إحصائيات النظام",
            "sidebar_processed": "التذاكر المعالجة",
            "sidebar_accuracy": "متوسط الثقة",
            "sidebar_actions": "إجراءات النظام",
            "sidebar_clear": "🔄 مسح السجل",
            "sidebar_view_logs": "📊 عرض سجلات التدقيق",
            "sidebar_status": "حالة النظام",
            "sidebar_ai_models": "نماذج الذكاء الاصطناعي",
            "sidebar_security": "الأمان",
            "sidebar_pii": "حماية المعلومات الشخصية",
            "sidebar_audit": "تسجيل التدقيق",
            
            # Ticket Input
            "section_examples": "تذاكر مثال",
            "section_input": "أدخل تفاصيل التذكرة",
            "example_select": "اختر تذكرة مثال:",
            "input_label": "نص التذكرة",
            "input_placeholder": "أدخل وصفاً مفصلاً للتذكرة...",
            "btn_analyze": "🔍 تحليل التذكرة",
            "btn_clear": "🧹 مسح المدخلات",
            "input_stats": "الحروف: {} | الكلمات: {}",
            
            # Example Tickets
            "example_emergency": "🚨 حالة طوارئ",
            "example_emergency_desc": "مشكلة سلامة حرجة تتطلب اهتماماً فورياً",
            "example_technical": "💻 مشكلة تقنية",
            "example_technical_desc": "مشكلة تقنية في البوابة الحكومية",
            "example_billing": "💰 مشكلة فاتورة",
            "example_billing_desc": "تحقيق في تناقض فاتورة المواطن",
            "example_facilities": "🏢 طلب مرافق",
            "example_facilities_desc": "طلب صيانة مبنى حكومي",
            "example_inquiry": "📋 استفسار خدمة",
            "example_inquiry_desc": "طلب خدمة المواطن للوثائق",
            
            # Analysis Results
            "results_title": "نتائج تحليل التذكرة",
            "results_ticket_id": "رقم التذكرة",
            "results_priority": "مستوى الأولوية",
            "results_response_time": "وقت الاستجابة",
            "results_department": "القسم",
            "results_confidence": "ثقة الذكاء الاصطناعي",
            "results_confidence_high": "ثقة عالية",
            "results_confidence_medium": "ثقة متوسطة",
            "results_confidence_low": "ثقة منخفضة",
            "results_sentiment": "مشاعر المواطن",
            "results_category": "الفئة",
            "results_manual_review": "مراجعة يدوية مطلوبة",
            "results_auto_processing": "تمت الموافقة على المعالجة التلقائية",
            "results_dissatisfaction": "تم اكتشاف عدم رضا المواطن",
            "results_positive_feedback": "تم استقبال تعليقات إيجابية",
            
            # Department
            "dept_assignment": "تعيين القسم",
            "dept_supervisor": "المشرف",
            "dept_contact": "معلومات الاتصال",
            "dept_phone": "الهاتف",
            "dept_email": "البريد الإلكتروني",
            "dept_action_required": "إجراء مطلوب",
            
            # Actions
            "actions_title": "الإجراءات المطلوبة",
            "action_emergency": "🚨 تفعيل بروتوكول الاستجابة للطوارئ",
            "action_technical": "💻 تعيين لفريق الدعم التقني",
            "action_billing": "💰 تحويل لقسم المالية",
            "action_facilities": "🔧 تعيين لفريق الصيانة",
            "action_inquiry": "📞 التواصل مع المواطن للتوضيح",
            "action_standard": "طابور المعالجة القياسي",
            
            # History Table
            "history_title": "سجل التذاكر",
            "history_time": "الوقت",
            "history_ticket_id": "رقم التذكرة",
            "history_category": "الفئة",
            "history_priority": "الأولوية",
            "history_status": "الحالة",
            "history_ai_action": "الإجراء المقترح من الذكاء الاصطناعي",
            "history_no_data": "لا يوجد سجل تذاكر متاح",
            "history_summary": "ملخص السجل",
            "history_total": "إجمالي التذاكر",
            "history_avg_conf": "متوسط الثقة",
            "history_critical": "الحالات الحرجة",
            "history_manual": "المراجعات اليدوية",
            
            # Status Messages
            "status_processing": "جاري تحليل التذكرة بنماذج الذكاء الاصطناعي...",
            "status_complete": "اكتمل التحليل!",
            "status_error_empty": "الرجاء إدخال نص التذكرة",
            "status_error_models": "لم يتم تحميل نماذج الذكاء الاصطناعي. الرجاء تدريب النماذج أولاً.",
            "status_success": "تم معالجة التذكرة بنجاح",
            
            # Footer
            "footer_title": "وزارة الذكاء الاصطناعي في الإمارات",
            "footer_subtitle": "مبادرة الحكومة الذكية • إنتاج آمن",
            "footer_copyright": "© 2024 حكومة الإمارات العربية المتحدة",
        }
    }
    
    def __init__(self, language: str = "en"):
        self.language = language
    
    def translate(self, key: str) -> str:
        """Translate a key to current language."""
        return self.TRANSLATIONS.get(self.language, {}).get(key, key)
    
    def t(self, key: str) -> str:
        """Shortcut method for translation (FIXED)."""
        return self.translate(key)
    
    def set_language(self, language: str):
        """Set language and update CSS."""
        if language in ["en", "ar"]:
            self.language = language

# ============================================
# UAE GOVERNMENT TICKET SYSTEM - FIXED VERSION
# ============================================
class UAEGovTicketSystem:
    """UAE Government AI Ticket Triage System - Fully Fixed Version."""
    
    def __init__(self):
        """Initialize system with proper state management."""
        self.processor = processor if MODELS_LOADED else None
        self.translator = UAEGovernmentTranslator("en")
        self._init_session_state()
    
    def _init_session_state(self):
        """Initialize session state with complete UI state."""
        # Language and UI state
        if 'language' not in st.session_state:
            st.session_state.language = "en"
        
        # Ticket data
        if 'ticket_history' not in st.session_state:
            st.session_state.ticket_history = []
        if 'current_result' not in st.session_state:
            st.session_state.current_result = None
        if 'ticket_text' not in st.session_state:
            st.session_state.ticket_text = ""
        if 'processing_times' not in st.session_state:
            st.session_state.processing_times = []
        
        # System configuration
        if 'confidence_threshold' not in st.session_state:
            st.session_state.confidence_threshold = 0.55
        if 'selected_example' not in st.session_state:
            st.session_state.selected_example = None
        if 'processing_in_progress' not in st.session_state:
            st.session_state.processing_in_progress = False
        
        # Update translator
        self.translator.set_language(st.session_state.language)
    
    def _apply_styles(self):
        """Apply CSS styles with RTL/LTR support and professional design."""
        css = f"""
        <style>
            /* UAE Government Colors - Professional Palette */
            :root {{
                --uae-green: #008000;
                --uae-green-dark: #006400;
                --uae-green-light: #E8F5E8;
                --uae-red: #DC2626;
                --uae-red-light: #FEE2E2;
                --uae-yellow: #F59E0B;
                --uae-yellow-light: #FEF3C7;
                --uae-blue: #2563EB;
                --uae-blue-light: #DBEAFE;
                --uae-gray: #6B7280;
                --uae-gray-light: #F9FAFB;
                --uae-white: #FFFFFF;
            }}
            
            /* Language-specific text direction */
            .text-direction-rtl {{
                direction: rtl;
                text-align: right;
                font-family: 'Segoe UI', 'Arial', sans-serif;
            }}
            
            .text-direction-ltr {{
                direction: ltr;
                text-align: left;
            }}
            
            /* Professional Government Header */
            .gov-header {{
                background: linear-gradient(90deg, var(--uae-green) 0%, var(--uae-green-dark) 100%);
                color: white;
                padding: 1.5rem 2rem;
                border-radius: 0 0 12px 12px;
                margin: -1rem -2rem 2rem -2rem;
                box-shadow: 0 4px 12px rgba(0, 128, 0, 0.15);
            }}
            
            /* Section Headers */
            .section-header {{
                color: var(--uae-green-dark);
                border-bottom: 3px solid var(--uae-green);
                padding-bottom: 0.75rem;
                margin-bottom: 1.5rem;
                font-weight: 700;
                font-size: 1.3rem;
            }}
            
            /* Priority Badges - Professional Design */
            .priority-badge {{
                padding: 6px 16px;
                border-radius: 20px;
                font-weight: 700;
                font-size: 0.85rem;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                display: inline-block;
                margin: 4px;
            }}
            
            .priority-critical {{
                background: linear-gradient(135deg, #DC2626, #EF4444);
                color: white;
                animation: pulse-critical 2s infinite;
            }}
            
            .priority-high {{
                background: linear-gradient(135deg, #EA580C, #F97316);
                color: white;
            }}
            
            .priority-medium {{
                background: linear-gradient(135deg, var(--uae-green), #10B981);
                color: white;
            }}
            
            .priority-low {{
                background: linear-gradient(135deg, #3B82F6, #60A5FA);
                color: white;
            }}
            
            @keyframes pulse-critical {{
                0% {{ box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.4); }}
                70% {{ box-shadow: 0 0 0 10px rgba(220, 38, 38, 0); }}
                100% {{ box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }}
            }}
            
            /* Confidence Indicators */
            .confidence-high {{ color: #10B981; font-weight: 700; }}
            .confidence-medium {{ color: #F59E0B; font-weight: 700; }}
            .confidence-low {{ color: #DC2626; font-weight: 700; }}
            
            /* Professional Government Cards */
            .gov-card {{
                background: white;
                border: 1px solid #E5E7EB;
                border-radius: 10px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                transition: all 0.2s ease;
            }}
            
            .gov-card:hover {{
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
                border-color: var(--uae-green-light);
            }}
            
            /* Action Items */
            .action-item {{
                background: var(--uae-green-light);
                border-left: 4px solid var(--uae-green);
                padding: 12px 16px;
                margin: 8px 0;
                border-radius: 6px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            
            /* Status Indicators */
            .status-indicator {{
                display: inline-flex;
                align-items: center;
                gap: 6px;
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 0.85rem;
                font-weight: 600;
            }}
            
            .status-success {{ background: #D1FAE5; color: #065F46; }}
            .status-warning {{ background: #FEF3C7; color: #92400E; }}
            .status-error {{ background: #FEE2E2; color: #991B1B; }}
            .status-info {{ background: #DBEAFE; color: #1E40AF; }}
            
            /* Button Styling */
            .stButton button {{
                background: linear-gradient(135deg, var(--uae-green), var(--uae-green-dark));
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: 600;
                padding: 12px 24px;
                transition: all 0.2s ease;
            }}
            
            .stButton button:hover {{
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0, 128, 0, 0.2);
            }}
            
            /* Text Area Styling */
            .stTextArea textarea {{
                font-size: 16px;
                line-height: 1.5;
                border: 2px solid #E5E7EB;
                border-radius: 8px;
                padding: 12px;
            }}
            
            .stTextArea textarea:focus {{
                border-color: var(--uae-green);
                box-shadow: 0 0 0 3px rgba(0, 128, 0, 0.1);
            }}
            
            /* Example Ticket Buttons */
            .example-ticket-btn {{
                background: white;
                border: 2px solid var(--uae-green-light);
                color: var(--uae-green-dark);
                padding: 1rem;
                border-radius: 10px;
                text-align: center;
                font-weight: 600;
                font-size: 0.95rem;
                transition: all 0.2s ease;
                cursor: pointer;
            }}
            
            .example-ticket-btn:hover {{
                background: var(--uae-green-light);
                border-color: var(--uae-green);
                transform: translateY(-2px);
            }}
            
            /* Footer Styling */
            .gov-footer {{
                background: var(--uae-gray-light);
                padding: 1.5rem;
                border-radius: 10px;
                margin-top: 3rem;
                border-top: 3px solid var(--uae-green-light);
            }}
        </style>
        """
        
        st.markdown(css, unsafe_allow_html=True)
    
    def _display_header(self):
        """Display professional government header with language support."""
        direction_class = "text-direction-rtl" if st.session_state.language == "ar" else "text-direction-ltr"
        
        st.markdown(f"""
        <div class="gov-header {direction_class}">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="font-size: 2.5rem;">🏛️</div>
                    <div>
                        <h1 style="margin: 0; font-size: 2rem;">{self.translator.t('app_title')}</h1>
                        <p style="margin: 0; opacity: 0.9; font-size: 1rem;">{self.translator.t('app_subtitle')}</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <div style="background: rgba(255, 255, 255, 0.2); padding: 8px 16px; border-radius: 20px; font-weight: 600;">
                        {self.translator.t('sidebar_system')}
                    </div>
                    <div style="font-size: 2rem;">🇦🇪</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def _display_sidebar(self):
        """Display sidebar with system controls - Fixed layout."""
        with st.sidebar:
            # Language Toggle
            st.markdown(f"### 🌐 {self.translator.t('sidebar_language')}")
            
            lang_col1, lang_col2 = st.columns(2)
            with lang_col1:
                if st.button("🇦🇪 عربي", use_container_width=True,
                           type="primary" if st.session_state.language == "ar" else "secondary"):
                    st.session_state.language = "ar"
                    self.translator.set_language("ar")
                    st.rerun()
            
            with lang_col2:
                if st.button("🇺🇸 English", use_container_width=True,
                           type="primary" if st.session_state.language == "en" else "secondary"):
                    st.session_state.language = "en"
                    self.translator.set_language("en")
                    st.rerun()
            
            st.divider()
            
            # Confidence Threshold
            st.markdown(f"#### 📊 {self.translator.t('sidebar_threshold')}")
            threshold = st.slider(
                self.translator.t('sidebar_threshold'),
                min_value=0.0,
                max_value=1.0,
                value=st.session_state.confidence_threshold,
                step=0.05,
                help=self.translator.t('sidebar_threshold_help'),
                label_visibility="collapsed"
            )
            
            if self.processor:
                self.processor.confidence_threshold = threshold
            st.session_state.confidence_threshold = threshold
            
            # User Role
            st.selectbox(
                self.translator.t('sidebar_user_role'),
                [
                    self.translator.t('sidebar_analyst'),
                    self.translator.t('sidebar_supervisor'),
                    self.translator.t('sidebar_admin')
                ],
                key="user_role_select"
            )
            
            st.divider()
            
            # System Statistics
            st.markdown(f"### 📈 {self.translator.t('sidebar_stats')}")
            
            stats_col1, stats_col2 = st.columns(2)
            with stats_col1:
                total = len(st.session_state.ticket_history)
                st.metric(self.translator.t('sidebar_processed'), total)
            
            with stats_col2:
                if total > 0:
                    recent = st.session_state.ticket_history[-5:]
                    avg_conf = np.mean([t.get('confidence', 0) for t in recent])
                    st.metric(self.translator.t('sidebar_accuracy'), f"{avg_conf:.1%}")
                else:
                    st.metric(self.translator.t('sidebar_accuracy'), "N/A")
            
            # Performance metrics
            if len(st.session_state.processing_times) > 0:
                avg_time = np.mean(st.session_state.processing_times[-5:])
                st.info(f"⏱️ Avg Processing: {avg_time:.2f}s")
            
            # Critical cases alert
            if total > 0:
                priorities = [t.get('priority', 'Medium') for t in st.session_state.ticket_history[-10:]]
                critical = priorities.count('Critical')
                if critical > 0:
                    st.warning(f"🚨 {critical} {self.translator.t('history_critical').lower()}")
            
            st.divider()
            
            # System Actions
            st.markdown(f"### ⚡ {self.translator.t('sidebar_actions')}")
            
            action_col1, action_col2 = st.columns(2)
            with action_col1:
                if st.button(self.translator.t('sidebar_clear'), use_container_width=True, type="secondary"):
                    st.session_state.ticket_history = []
                    st.session_state.current_result = None
                    st.session_state.ticket_text = ""
                    st.session_state.processing_times = []
                    st.rerun()
            
            with action_col2:
                if st.button(self.translator.t('sidebar_view_logs'), use_container_width=True, type="secondary"):
                    try:
                        log_file = Path("../logs/system_audit.log")
                        if log_file.exists():
                            with open(log_file, 'r') as f:
                                logs = f.readlines()[-15:]
                            with st.expander("🔍 Audit Logs", expanded=True):
                                st.code("\n".join(logs), language="json")
                        else:
                            st.info("No audit logs available yet.")
                    except Exception as e:
                        st.error(f"Unable to access logs: {str(e)}")
            
            st.divider()
            
            # System Status
            st.markdown(f"### 🟢 {self.translator.t('sidebar_status')}")
            
            status_col1, status_col2 = st.columns(2)
            with status_col1:
                if MODELS_LOADED:
                    st.success("✅ AI Models")
                else:
                    st.error("❌ AI Models")
                st.caption(self.translator.t('sidebar_ai_models'))
            
            with status_col2:
                st.success("✅ Security")
                st.caption(self.translator.t('sidebar_security'))
    
    def _get_example_tickets(self) -> List[Dict[str, str]]:
        """Get comprehensive example tickets with translations."""
        examples = [
            {
                "title_key": "example_emergency",
                "desc_key": "example_emergency_desc",
                "text_en": "URGENT: Fire alarm system malfunction at Ministry of AI building, Dubai Internet City. Multiple floors affected. People reporting smoke smell. Emirates ID: 784-1990-1234567-1. Contact: +971501234567. Need immediate emergency response team deployment.",
                "text_ar": "عاجل: عطل في نظام إنذار الحريق في مبنى وزارة الذكاء الاصطناعي، دبي إنترنت سيتي. طوابق متعددة متأثرة. أشخاص يبلغون عن رائحة دخان. رقم الهوية: 784-1990-1234567-1. الاتصال: +971501234567. يحتاج إلى نشر فريق الاستجابة للطوارئ فوراً."
            },
            {
                "title_key": "example_technical",
                "desc_key": "example_technical_desc",
                "text_en": "DEWA online payment portal not working since 9:00 AM. Users receiving 'Error 500: Internal Server Error' when trying to pay bills. Issue affecting all customers in Dubai area. Need urgent technical team intervention to restore service.",
                "text_ar": "بوابة الدفع الإلكتروني لهيئة كهرباء ومياه دبي لا تعمل منذ الساعة 9:00 صباحاً. المستخدمون يتلقون 'خطأ 500: خطأ في الخادم الداخلي' عند محاولة دفع الفواتير. المشكلة تؤثر على جميع العملاء في منطقة دبي. يحتاج إلى تدخل فوري من الفريق التقني لاستعادة الخدمة."
            },
            {
                "title_key": "example_billing",
                "desc_key": "example_billing_desc",
                "text_en": "Incorrect charges on Etisalat invoice for November 2024. Bill shows 750 AED for international calls to USA, but no international calls were made from my number +971501234567. Need detailed call logs and immediate correction of charges.",
                "text_ar": "رسوم غير صحيحة على فاتورة اتصالات لشهر نوفمبر 2024. الفاتورة تظهر 750 درهماً لمكالمات دولية إلى الولايات المتحدة، ولكن لم تجر أي مكالمات دولية من رقمي +971501234567. يحتاج إلى سجلات مكالمات مفصلة وتصحيح فوري للرسوم."
            },
            {
                "title_key": "example_facilities",
                "desc_key": "example_facilities_desc",
                "text_en": "Air conditioning system malfunction in Dubai Government Customer Happiness Center, Al Barsha. Temperature reading 30°C inside building, causing discomfort for visitors and staff. Urgent maintenance required. Building ID: DXB-GOV-0456.",
                "text_ar": "عطل في نظام التكييف في مركز سعادة المتعاملين الحكومي بدبي، البرشاء. قراءة درجة الحرارة 30° مئوية داخل المبنى، مما يسبب عدم راحة للزوار والموظفين. يحتاج إلى صيانة عاجلة. رقم المبنى: DXB-GOV-0456."
            },
            {
                "title_key": "example_inquiry",
                "desc_key": "example_inquiry_desc",
                "text_en": "Need to inquire about Emirates ID renewal process for family of 4. What documents are required? What is the processing time? My Emirates ID: 784-1995-5678901-5. Please provide step-by-step guidance and appointment scheduling options.",
                "text_ar": "أحتاج إلى الاستفسار عن عملية تجديد هوية الإمارات لعائلة مكونة من 4 أفراد. ما هي المستندات المطلوبة؟ ما هو وقت المعالجة؟ رقم هوية الإمارات الخاصة بي: 784-1995-5678901-5. يرجى تقديم إرشادات خطوة بخطوة وخيارات جدولة المواعيد."
            }
        ]
        
        # Translate all example data
        for example in examples:
            example["title"] = self.translator.t(example["title_key"])
            example["description"] = self.translator.t(example["desc_key"])
            example["text"] = example["text_ar"] if st.session_state.language == "ar" else example["text_en"]
        
        return examples
    
    def _display_ticket_input_section(self):
        """Display ticket input section with examples - Fixed layout."""
        # Example Tickets Section
        st.markdown(f"### 📋 {self.translator.t('section_examples')}")
        st.markdown(self.translator.t('example_select'))
        
        examples = self._get_example_tickets()
        
        # Display 3 example buttons per row - No nested columns
        for i in range(0, len(examples), 3):
            row_examples = examples[i:i+3]
            cols = st.columns(len(row_examples))
            
            for idx, (col, example) in enumerate(zip(cols, row_examples)):
                with col:
                    # Display example button with proper styling
                    if st.button(
                        example["title"],
                        key=f"example_{i+idx}",
                        help=example["description"],
                        use_container_width=True
                    ):
                        st.session_state.ticket_text = example["text"]
                        st.session_state.selected_example = example["title_key"]
                        st.rerun()
        
        # Show selected example preview
        if st.session_state.selected_example:
            selected = next((e for e in examples if e["title_key"] == st.session_state.selected_example), None)
            if selected:
                with st.expander(f"📄 Preview: {selected['title']}", expanded=True):
                    st.info(selected["text"])
                    if st.button("🚀 Analyze This Example", type="primary", use_container_width=True):
                        self._process_ticket(selected["text"])
        
        st.divider()
        
        # Ticket Input Section
        st.markdown(f"### 📝 {self.translator.t('section_input')}")
        
        # Text area with language direction
        text_dir = "rtl" if st.session_state.language == "ar" else "ltr"
        ticket_text = st.text_area(
            self.translator.t('input_label'),
            value=st.session_state.ticket_text,
            height=200,
            placeholder=self.translator.t('input_placeholder'),
            key="ticket_input_area",
            help="Enter complete ticket details. AI will automatically protect sensitive information."
        )
        
        st.session_state.ticket_text = ticket_text
        
        # Input statistics and action buttons
        btn_col1, btn_col2, btn_col3 = st.columns([2, 1, 1])
        
        with btn_col1:
            if ticket_text.strip():
                chars = len(ticket_text)
                words = len(ticket_text.split())
                st.caption(self.translator.t('input_stats').format(chars, words))
            else:
                st.caption("Enter ticket text to begin analysis")
        
        with btn_col2:
            analyze_disabled = not ticket_text.strip() or not MODELS_LOADED or st.session_state.processing_in_progress
            if st.button(
                self.translator.t('btn_analyze'),
                disabled=analyze_disabled,
                use_container_width=True,
                type="primary" if not analyze_disabled else "secondary"
            ):
                self._process_ticket(ticket_text)
        
        with btn_col3:
            if st.button(self.translator.t('btn_clear'), use_container_width=True, type="secondary"):
                st.session_state.ticket_text = ""
                st.session_state.selected_example = None
                st.rerun()
    
    def _get_ai_action(self, result: Dict) -> str:
        """Get AI suggested action from results - FIXED implementation."""
        decisions = result['final_decisions']
        
        # Map actions based on priority and category
        if decisions['priority'] == 'Critical':
            return self.translator.t('action_emergency')
        elif decisions['category'] == 'Technical / IT':
            return self.translator.t('action_technical')
        elif decisions['category'] == 'Billing':
            return self.translator.t('action_billing')
        elif decisions['category'] == 'Facilities':
            return self.translator.t('action_facilities')
        elif decisions['category'] == 'Inquiry':
            return self.translator.t('action_inquiry')
        elif decisions['sentiment'] == 'Negative':
            return self.translator.t('action_inquiry')  # Contact for negative sentiment
        else:
            return self.translator.t('action_standard')
    
    def _process_ticket(self, text: str):
        """Process a ticket with proper error handling and performance tracking."""
        if not text.strip():
            st.error(self.translator.t('status_error_empty'))
            return
        
        if not self.processor:
            st.error(self.translator.t('status_error_models'))
            return
        
        # Set processing flag
        st.session_state.processing_in_progress = True
        
        try:
            # Show processing animation
            with st.spinner(f"⏳ {self.translator.t('status_processing')}"):
                # Simulate processing steps for better UX
                progress_text = st.empty()
                progress_bar = st.progress(0)
                
                steps = ["Analyzing text...", "Checking for sensitive data...", 
                        "Running AI models...", "Applying business rules..."]
                
                for i, step in enumerate(steps):
                    progress_text.text(f"⏳ {step}")
                    progress_bar.progress((i + 1) / len(steps))
                    time.sleep(0.3)
                
                # Actual processing
                start_time = time.time()
                result = self.processor.process_text(text.strip())
                processing_time = time.time() - start_time
                
                # Store processing time
                st.session_state.processing_times.append(processing_time)
                if len(st.session_state.processing_times) > 50:
                    st.session_state.processing_times = st.session_state.processing_times[-50:]
                
                # Get AI action
                ai_action = self._get_ai_action(result)
                
                # Create comprehensive history entry
                history_entry = {
                    'timestamp': datetime.now().strftime("%H:%M:%S"),
                    'date': datetime.now().strftime("%Y-%m-%d"),
                    'ticket_id': result['final_decisions']['ticket_id'],
                    'category': result['final_decisions']['category'],
                    'sentiment': result['final_decisions']['sentiment'],
                    'priority': result['final_decisions']['priority'],
                    'confidence': result['final_decisions']['confidence_score'],
                    'department': result['final_decisions']['department'],
                    'processing_time': processing_time,
                    'needs_review': result['final_decisions']['needs_manual_review'],
                    'pii_detected': result['pii_protection']['has_pii'],
                    'ai_action': ai_action,
                    'status': 'Manual Review' if result['final_decisions']['needs_manual_review'] else 'Auto-Processed'
                }
                
                # Add to history
                st.session_state.ticket_history.append(history_entry)
                if len(st.session_state.ticket_history) > 100:
                    st.session_state.ticket_history = st.session_state.ticket_history[-100:]
                
                # Store current result
                st.session_state.current_result = result
                
                # Clear processing indicators
                progress_text.empty()
                progress_bar.empty()
                
                # Show success message
                st.success(f"✅ {self.translator.t('status_complete')}")
                st.toast(f"{self.translator.t('status_success')}: {history_entry['ticket_id']}")
                
        except Exception as e:
            st.error(f"❌ Processing error: {str(e)}")
            st.info("Please try again or contact system administrator")
        
        finally:
            # Reset processing flag
            st.session_state.processing_in_progress = False
    
    def _display_ticket_results(self):
        """Display analysis results - Fixed with comprehensive data."""
        if not st.session_state.current_result:
            return
        
        result = st.session_state.current_result
        decisions = result['final_decisions']
        ml_results = result['ml_predictions']
        pii_info = result['pii_protection']
        safety_info = result['safety_check']
        
        st.markdown(f"### 📊 {self.translator.t('results_title')}")
        
        # Results metrics in 4 columns - No nesting
        res_col1, res_col2, res_col3, res_col4 = st.columns(4)
        
        with res_col1:
            st.markdown('<div class="gov-card">', unsafe_allow_html=True)
            st.markdown(f"**{self.translator.t('results_ticket_id')}**")
            st.code(decisions['ticket_id'], language="text")
            st.markdown(f"**Processed:** {result['ticket_processing']['timestamp'].split('T')[0]}")
            if 'processing_time' in result:
                st.markdown(f"**Duration:** {result['processing_time']:.2f}s")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with res_col2:
            st.markdown('<div class="gov-card">', unsafe_allow_html=True)
            st.markdown(f"**{self.translator.t('results_priority')}**")
            
            priority = decisions['priority']
            priority_class = f"priority-{priority.lower()}"
            st.markdown(f'<div class="{priority_class}">{priority}</div>', unsafe_allow_html=True)
            
            st.markdown(f"**{self.translator.t('results_response_time')}:** {decisions['response_time']}")
            st.markdown(f"**{self.translator.t('results_department')}:** {decisions['department']}")
            
            # Safety override indicator
            if safety_info['needs_override'] and not safety_info['is_spam']:
                st.markdown('<div class="status-warning status-indicator">🚨 Safety Override</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with res_col3:
            st.markdown('<div class="gov-card">', unsafe_allow_html=True)
            st.markdown(f"**{self.translator.t('results_confidence')}**")
            
            conf = decisions['confidence_score']
            if conf >= 0.8:
                conf_class = "confidence-high"
                conf_label = self.translator.t('results_confidence_high')
                icon = "🟢"
            elif conf >= 0.55:
                conf_class = "confidence-medium"
                conf_label = self.translator.t('results_confidence_medium')
                icon = "🟡"
            else:
                conf_class = "confidence-low"
                conf_label = self.translator.t('results_confidence_low')
                icon = "🔴"
            
            st.markdown(f'<div class="{conf_class}">{icon} {conf:.1%}</div>', unsafe_allow_html=True)
            st.markdown(f'<div>{conf_label}</div>', unsafe_allow_html=True)
            
            if decisions['needs_manual_review']:
                st.markdown('<div class="status-error status-indicator">⚠️ {}</div>'.format(
                    self.translator.t('results_manual_review')), unsafe_allow_html=True)
                if decisions['manual_review_reason']:
                    st.caption(f"Reason: {decisions['manual_review_reason']}")
            else:
                st.markdown('<div class="status-success status-indicator">✅ {}</div>'.format(
                    self.translator.t('results_auto_processing')), unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with res_col4:
            st.markdown('<div class="gov-card">', unsafe_allow_html=True)
            st.markdown(f"**{self.translator.t('results_sentiment')}**")
            
            sentiment = decisions['sentiment']
            sentiment_map = {
                'Positive': ('😊', self.translator.t('results_positive_feedback'), '#10B981'),
                'Neutral': ('😐', 'Neutral', '#6B7280'),
                'Negative': ('😠', self.translator.t('results_dissatisfaction'), '#DC2626')
            }
            icon, sentiment_text, color = sentiment_map.get(sentiment, ('😐', 'Neutral', '#6B7280'))
            
            st.markdown(f'<div style="font-size: 1.8rem; color: {color}; font-weight: 700; margin: 10px 0;">{icon} {sentiment_text}</div>', 
                       unsafe_allow_html=True)
            
            st.markdown(f"**{self.translator.t('results_category')}:** {decisions['category']}")
            if 'category_confidence' in ml_results:
                st.caption(f"Confidence: {ml_results['category_confidence']:.1%}")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Department and Actions in 2 columns
        st.markdown(f"### 🏢 {self.translator.t('dept_assignment')}")
        
        dept_col1, dept_col2 = st.columns(2)
        
        with dept_col1:
            st.markdown('<div class="gov-card">', unsafe_allow_html=True)
            st.markdown(f"**{decisions['department']}**")
            st.markdown(f"**{self.translator.t('dept_supervisor')}:** {decisions['department_contact']['supervisor']}")
            st.markdown(f"**{self.translator.t('dept_phone')}:** {decisions['department_contact']['phone']}")
            st.markdown(f"**{self.translator.t('dept_email')}:** {decisions['department_contact']['email']}")
            
            # PII protection status
            if pii_info['has_pii']:
                st.markdown('<div class="status-success status-indicator">✅ PII Protected</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="status-info status-indicator">ℹ️ No PII Detected</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with dept_col2:
            st.markdown('<div class="gov-card">', unsafe_allow_html=True)
            st.markdown(f"**{self.translator.t('actions_title')}**")
            
            if decisions['action_items']:
                for i, action in enumerate(decisions['action_items'], 1):
                    st.markdown(f'<div class="action-item"><span style="font-weight: 700;">{i}.</span> {action}</div>', 
                              unsafe_allow_html=True)
            else:
                st.info("No specific actions required")
            
            # Response timeline
            if decisions.get('response_time'):
                st.markdown(f"**⏱️ {self.translator.t('results_response_time')}:** {decisions['response_time']}")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    def _display_ticket_history_table(self):
        """Display ticket history table using st.dataframe() - Fixed implementation."""
        st.markdown(f"### 📚 {self.translator.t('history_title')}")
        
        if not st.session_state.ticket_history:
            st.info(self.translator.t('history_no_data'))
            return
        
        # Prepare data for dataframe
        history_data = []
        for ticket in st.session_state.ticket_history[-20:]:  # Last 20 tickets
            # Get status indicator
            if ticket.get('needs_review', False):
                status = "⚠️ Manual"
                status_color = "#DC2626"
            else:
                status = "✅ Auto"
                status_color = "#10B981"
            
            # Get priority badge
            priority = ticket['priority']
            priority_map = {
                'Critical': '🔴',
                'High': '🟠', 
                'Medium': '🟢',
                'Low': '🔵'
            }
            priority_icon = priority_map.get(priority, '🟢')
            
            history_data.append({
                self.translator.t('history_time'): ticket['timestamp'],
                self.translator.t('history_ticket_id'): ticket['ticket_id'],
                self.translator.t('history_category'): ticket['category'],
                self.translator.t('history_priority'): f"{priority_icon} {priority}",
                self.translator.t('history_status'): status,
                self.translator.t('history_ai_action'): ticket['ai_action']
            })
        
        # Create and display dataframe
        df = pd.DataFrame(history_data)
        
        # Display with professional styling
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                self.translator.t('history_time'): st.column_config.TextColumn(
                    self.translator.t('history_time'),
                    width="small"
                ),
                self.translator.t('history_ticket_id'): st.column_config.TextColumn(
                    self.translator.t('history_ticket_id'),
                    width="medium"
                ),
                self.translator.t('history_category'): st.column_config.TextColumn(
                    self.translator.t('history_category'),
                    width="medium"
                ),
                self.translator.t('history_priority'): st.column_config.TextColumn(
                    self.translator.t('history_priority'),
                    width="small"
                ),
                self.translator.t('history_status'): st.column_config.TextColumn(
                    self.translator.t('history_status'),
                    width="small"
                ),
                self.translator.t('history_ai_action'): st.column_config.TextColumn(
                    self.translator.t('history_ai_action'),
                    width="large"
                )
            }
        )
        
        # History summary
        if st.session_state.ticket_history:
            st.markdown(f"#### 📊 {self.translator.t('history_summary')}")
            
            summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)
            
            recent = st.session_state.ticket_history[-15:]
            
            with summary_col1:
                total = len(recent)
                st.metric(self.translator.t('history_total'), total)
            
            with summary_col2:
                avg_conf = np.mean([t['confidence'] for t in recent]) if recent else 0
                st.metric(self.translator.t('history_avg_conf'), f"{avg_conf:.1%}")
            
            with summary_col3:
                critical = sum(1 for t in recent if t['priority'] == 'Critical')
                st.metric(self.translator.t('history_critical'), critical)
            
            with summary_col4:
                manual = sum(1 for t in recent if t.get('needs_review', False))
                st.metric(self.translator.t('history_manual'), manual)
    
    def _display_footer(self):
        """Display professional government footer."""
        direction_class = "text-direction-rtl" if st.session_state.language == "ar" else "text-direction-ltr"
        
        st.markdown(f"""
        <div class="gov-footer {direction_class}">
            <div style="text-align: center;">
                <div style="display: flex; justify-content: center; gap: 1rem; margin-bottom: 1rem; font-size: 1.5rem;">
                    <span>🏛️</span>
                    <span>🤖</span>
                    <span>🇦🇪</span>
                </div>
                <p style="color: var(--uae-green-dark); font-weight: 700; margin-bottom: 0.5rem;">
                    {self.translator.t('footer_title')}
                </p>
                <p style="color: var(--uae-gray); font-size: 0.9rem; margin-bottom: 0.5rem;">
                    {self.translator.t('footer_subtitle')} • Python 3.12.7 • Streamlit 1.31.0
                </p>
                <p style="color: var(--uae-gray); font-size: 0.8rem;">
                    {self.translator.t('footer_copyright')} • All Rights Reserved
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def run(self):
        """Main application runner - Professional implementation."""
        # Apply styles
        self._apply_styles()
        
        # Display header
        self._display_header()
        
        # Create main layout - ONE LEVEL OF COLUMNS ONLY
        main_col1, main_col2 = st.columns([1, 4])
        
        with main_col1:
            self._display_sidebar()
        
        with main_col2:
            # Use tabs for main content
            tab1, tab2 = st.tabs([
                self.translator.t('tab_analyze'),
                self.translator.t('tab_history')
            ])
            
            with tab1:
                # Ticket input section
                self._display_ticket_input_section()
                
                # Display results if available
                if st.session_state.current_result:
                    st.divider()
                    self._display_ticket_results()
            
            with tab2:
                # Ticket history table
                self._display_ticket_history_table()
        
        # Footer
        st.divider()
        self._display_footer()

# ============================================
# MAIN APPLICATION ENTRY POINT
# ============================================
def main():
    """Main entry point - Enterprise ready."""
    try:
        # Initialize Streamlit page
        st.set_page_config(
            page_title="UAE Government AI Ticket Triage",
            page_icon="🏛️",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                'Get Help': 'https://www.ai.gov.ae',
                'About': "UAE Government AI System v2.4.0 | Production Environment"
            }
        )
        
        # Initialize and run application
        app = UAEGovTicketSystem()
        app.run()
        
    except KeyboardInterrupt:
        st.info("🚫 Application interrupted by user")
    except Exception as e:
        # Professional error handling
        st.error(f"""
        ## ⚠️ **Critical System Error**
        
        The application encountered an unexpected error that prevented startup.
        
        **Error Details:**
        ```
        {str(e)}
        ```
        
        **Immediate Troubleshooting:**
        1. **Check Dependencies:** Run `pip install -r requirements.txt`
        2. **Train Models:** Run `python src/model_train.py`
        3. **Verify Data:** Ensure `data/tickets_synthetic_v2.csv` exists
        4. **Check Python:** Ensure Python 3.12.7 is installed
        
        **System Information:**
        - Python: {sys.version}
        - Streamlit: {st.__version__ if 'st' in locals() else 'Unknown'}
        
        **Support Contact:** ai-support@gov.ae | Emergency: 800-AI-HELP
        """)

if __name__ == "__main__":
    main()