"""
Complete Bilingual Translation System for UAE Government
نظام الترجمة الثنائية الكامل لحكومة الإمارات
"""

class TranslationSystem:
    """Complete translation system for UAE Government application."""
    
    # Complete translation dictionary
    TRANSLATIONS = {
        'en': {
            # Application
            'app_title': 'UAE Smart Government Ticket Intelligence',
            'app_subtitle': 'Ministry of Artificial Intelligence • United Arab Emirates',
            
            # Navigation
            'nav_new_ticket': 'New Ticket',
            'nav_history': 'History',
            'nav_analytics': 'Analytics',
            'nav_settings': 'Settings',
            
            # Sidebar
            'sidebar_configuration': 'System Configuration',
            'sidebar_threshold': 'Manual Review Threshold',
            'sidebar_user_role': 'User Role',
            'sidebar_language': 'Language',
            'sidebar_statistics': 'System Statistics',
            'sidebar_tickets_processed': 'Tickets Processed',
            'sidebar_avg_confidence': 'Average Confidence',
            'sidebar_quick_actions': 'Quick Actions',
            'sidebar_clear_session': 'Clear Session',
            'sidebar_view_logs': 'View Audit Log',
            'sidebar_system_status': 'System Status',
            'sidebar_ai_models': 'AI Models',
            'sidebar_category': 'Category',
            'sidebar_sentiment': 'Sentiment',
            'sidebar_security': 'Security',
            'sidebar_pii_protection': 'PII Protection',
            'sidebar_audit_log': 'Audit Log',
            'sidebar_version': 'Version 2.3.0 • Secure Network',
            'sidebar_copyright': '© 2024 UAE Government AI',
            
            # Main Content
            'content_example_tickets': 'Example Tickets',
            'content_click_to_load': 'Click any example to load it',
            'content_new_ticket_entry': 'New Ticket Entry',
            'content_enter_ticket': 'Enter Citizen Ticket Details',
            'content_ticket_text': 'Citizen Ticket Text',
            'content_placeholder': 'Enter citizen complaint, inquiry, or service request...',
            'content_auto_analyze': 'Auto-Analyze',
            'content_process_now': 'Process Now',
            'content_ticket_summary': 'Ticket Summary',
            'content_processing_time': 'Processing Time',
            'content_confidence_level': 'Confidence Level',
            'content_high_confidence': 'High Confidence',
            'content_medium_confidence': 'Medium Confidence',
            'content_low_confidence': 'Low Confidence',
            'content_auto_processing': 'Auto-Processing Approved',
            'content_citizen_sentiment': 'Citizen Sentiment',
            'content_citizen_dissatisfaction': 'Citizen dissatisfaction detected',
            'content_positive_feedback': 'Positive citizen feedback',
            'content_classification': 'Classification',
            'content_category': 'Category',
            'content_view_probabilities': 'View Category Probabilities',
            'content_priority_level': 'Priority Level',
            'content_target_response': 'Target Response',
            'content_emergency_protocol': 'Emergency Protocol',
            'content_emergency_override': 'EMERGENCY OVERRIDE ACTIVATED',
            'content_safety_keywords': 'Safety Keywords Detected',
            'content_response_time': 'Response Time',
            'content_immediate_action': 'IMMEDIATE ACTION REQUIRED',
            'content_department_assignment': 'Department Assignment',
            'content_responsible_supervisor': 'Responsible Supervisor',
            'content_contact_information': 'Contact Information',
            'content_phone': 'Phone',
            'content_email': 'Email',
            'content_department': 'Department',
            'content_action_items': 'Action Items',
            'content_manual_review': 'MANUAL REVIEW REQUIRED',
            'content_security_compliance': 'Security & Compliance',
            'content_pii_protection': 'PII Protection',
            'content_compliance_status': 'Compliance Status',
            'content_uae_data_law': 'UAE Data Protection Law',
            'content_gdpr_standards': 'GDPR Standards',
            'content_secure_processing': 'Secure Processing',
            'content_ai_analysis': 'AI Analysis Details',
            'content_category_confidence': 'Category Confidence',
            'content_sentiment_confidence': 'Sentiment Confidence',
            'content_view_details': 'View Processing Details',
            'content_recent_history': 'Recent History',
            
            # Categories
            'category_facilities': 'Facilities',
            'category_technical': 'Technical / IT',
            'category_billing': 'Billing',
            'category_inquiry': 'Inquiry',
            'category_safety': 'Safety / Emergency',
            
            # Sentiments
            'sentiment_positive': 'Positive',
            'sentiment_neutral': 'Neutral',
            'sentiment_negative': 'Negative',
            
            # Priorities
            'priority_critical': 'Critical',
            'priority_high': 'High',
            'priority_medium': 'Medium',
            'priority_low': 'Low',
            
            # Departments
            'department_emergency': 'Emergency Response Center',
            'department_it': 'IT Support Division',
            'department_finance': 'Finance & Accounts Department',
            'department_municipal': 'Municipal Services Department',
            'department_customer': 'Customer Service Center',
            'department_escalation': 'Priority Escalation Team',
            
            # Buttons & Actions
            'button_analyze': 'Analyze',
            'button_clear': 'Clear',
            'button_save': 'Save',
            'button_cancel': 'Cancel',
            'button_submit': 'Submit',
            'button_view_more': 'View More',
            'button_download': 'Download',
            
            # Messages
            'msg_processing': 'Analyzing with AI...',
            'msg_complete': 'Analysis Complete!',
            'msg_enter_text': 'Please enter ticket text',
            'msg_no_history': 'No processing history available',
            'msg_error': 'System Error',
            'msg_troubleshoot': 'Troubleshooting Steps',
            
            # Example Tickets
            'example_emergency': '🚨 Emergency Case',
            'example_emergency_text': 'URGENT: Fire alarm malfunction in government building...',
            'example_technical': '💻 Technical Issue',
            'example_technical_text': 'DEWA website not working for bill payment...',
            'example_billing': '💰 Billing Problem',
            'example_billing_text': 'Incorrect charges on my Etisalat bill...',
            'example_positive': '😊 Positive Feedback',
            'example_positive_text': 'Excellent service at RTA customer center...',
            'example_safety': '⚠️ Safety Concern',
            'example_safety_text': 'Gas smell detected near ADNOC station...',
            'example_inquiry': '❓ General Inquiry',
            'example_inquiry_text': 'What documents are needed for Emirates ID renewal...',
        },
        
        'ar': {
            # Application
            'app_title': 'نظام ذكاء التذاكر الحكومي الذكي',
            'app_subtitle': 'وزارة الذكاء الاصطناعي • الإمارات العربية المتحدة',
            
            # Navigation
            'nav_new_ticket': 'تذكرة جديدة',
            'nav_history': 'السجل',
            'nav_analytics': 'التحليلات',
            'nav_settings': 'الإعدادات',
            
            # Sidebar
            'sidebar_configuration': 'تكوين النظام',
            'sidebar_threshold': 'حد المراجعة اليدوية',
            'sidebar_user_role': 'دور المستخدم',
            'sidebar_language': 'اللغة',
            'sidebar_statistics': 'إحصائيات النظام',
            'sidebar_tickets_processed': 'التذاكر المعالجة',
            'sidebar_avg_confidence': 'متوسط الثقة',
            'sidebar_quick_actions': 'إجراءات سريعة',
            'sidebar_clear_session': 'مسح الجلسة',
            'sidebar_view_logs': 'عرض سجل التدقيق',
            'sidebar_system_status': 'حالة النظام',
            'sidebar_ai_models': 'نماذج الذكاء الاصطناعي',
            'sidebar_category': 'التصنيف',
            'sidebar_sentiment': 'المشاعر',
            'sidebar_security': 'الأمن',
            'sidebar_pii_protection': 'حماية المعلومات الشخصية',
            'sidebar_audit_log': 'سجل التدقيق',
            'sidebar_version': 'الإصدار 2.3.0 • شبكة آمنة',
            'sidebar_copyright': '© 2024 حكومة الإمارات الذكاء الاصطناعي',
            
            # Main Content
            'content_example_tickets': 'تذاكر مثال',
            'content_click_to_load': 'انقر على أي مثال لتحميله',
            'content_new_ticket_entry': 'إدخال تذكرة جديدة',
            'content_enter_ticket': 'أدخل تفاصيل تذكرة المواطن',
            'content_ticket_text': 'نص تذكرة المواطن',
            'content_placeholder': 'أدخل شكوى المواطن، استفسار، أو طلب خدمة...',
            'content_auto_analyze': 'تحليل تلقائي',
            'content_process_now': 'معالجة الآن',
            'content_ticket_summary': 'ملخص التذكرة',
            'content_processing_time': 'وقت المعالجة',
            'content_confidence_level': 'مستوى الثقة',
            'content_high_confidence': 'ثقة عالية',
            'content_medium_confidence': 'ثقة متوسطة',
            'content_low_confidence': 'ثقة منخفضة',
            'content_auto_processing': 'تمت الموافقة على المعالجة التلقائية',
            'content_citizen_sentiment': 'مشاعر المواطن',
            'content_citizen_dissatisfaction': 'تم اكتشاف عدم رضا المواطن',
            'content_positive_feedback': 'تم استقبال تعليقات إيجابية',
            'content_classification': 'التصنيف',
            'content_category': 'الفئة',
            'content_view_probabilities': 'عرض احتمالات الفئة',
            'content_priority_level': 'مستوى الأولوية',
            'content_target_response': 'وقت الاستجابة المستهدف',
            'content_emergency_protocol': 'بروتوكول الطوارئ',
            'content_emergency_override': 'تم تفعيل تجاوز الطوارئ',
            'content_safety_keywords': 'كلمات السلامة المكتشفة',
            'content_response_time': 'وقت الاستجابة',
            'content_immediate_action': 'إجراء فوري مطلوب',
            'content_department_assignment': 'تعيين القسم',
            'content_responsible_supervisor': 'المشرف المسؤول',
            'content_contact_information': 'معلومات الاتصال',
            'content_phone': 'الهاتف',
            'content_email': 'البريد الإلكتروني',
            'content_department': 'القسم',
            'content_action_items': 'بنود العمل',
            'content_manual_review': 'مراجعة يدوية مطلوبة',
            'content_security_compliance': 'الأمن والامتثال',
            'content_pii_protection': 'حماية المعلومات الشخصية',
            'content_compliance_status': 'حالة الامتثال',
            'content_uae_data_law': 'قانون حماية البيانات في الإمارات',
            'content_gdpr_standards': 'معايير GDPR',
            'content_secure_processing': 'معالجة آمنة',
            'content_ai_analysis': 'تفاصيل تحليل الذكاء الاصطناعي',
            'content_category_confidence': 'ثقة التصنيف',
            'content_sentiment_confidence': 'ثقة المشاعر',
            'content_view_details': 'عرض تفاصيل المعالجة',
            'content_recent_history': 'السجل الحديث',
            
            # Categories
            'category_facilities': 'المرافق',
            'category_technical': 'التقنية / تكنولوجيا المعلومات',
            'category_billing': 'الفواتير',
            'category_inquiry': 'الاستفسار',
            'category_safety': 'السلامة / الطوارئ',
            
            # Sentiments
            'sentiment_positive': 'إيجابي',
            'sentiment_neutral': 'محايد',
            'sentiment_negative': 'سلبي',
            
            # Priorities
            'priority_critical': 'حرج',
            'priority_high': 'عالي',
            'priority_medium': 'متوسط',
            'priority_low': 'منخفض',
            
            # Departments
            'department_emergency': 'مركز الاستجابة للطوارئ',
            'department_it': 'قسم الدعم التقني',
            'department_finance': 'قسم المالية والمحاسبة',
            'department_municipal': 'قسم الخدمات البلدية',
            'department_customer': 'مركز خدمة العملاء',
            'department_escalation': 'فريق التصعيد ذات الأولوية',
            
            # Buttons & Actions
            'button_analyze': 'تحليل',
            'button_clear': 'مسح',
            'button_save': 'حفظ',
            'button_cancel': 'إلغاء',
            'button_submit': 'إرسال',
            'button_view_more': 'عرض المزيد',
            'button_download': 'تحميل',
            
            # Messages
            'msg_processing': 'جاري التحليل بالذكاء الاصطناعي...',
            'msg_complete': 'تم التحليل بنجاح!',
            'msg_enter_text': 'الرجاء إدخال نص التذكرة',
            'msg_no_history': 'لا يوجد سجل معالجة متاح',
            'msg_error': 'خطأ في النظام',
            'msg_troubleshoot': 'خطوات استكشاف الأخطاء وإصلاحها',
            
            # Example Tickets
            'example_emergency': '🚨 حالة طوارئ',
            'example_emergency_text': 'عاجل: عطل في إنذار الحريق في مبنى حكومي...',
            'example_technical': '💻 مشكلة تقنية',
            'example_technical_text': 'موقع DEWA لا يعمل لدفع الفواتير...',
            'example_billing': '💰 مشكلة في الفاتورة',
            'example_billing_text': 'رسوم غير صحيحة في فاتورة الاتصالات...',
            'example_positive': '😊 تعليق إيجابي',
            'example_positive_text': 'خدمة ممتازة في مركز خدمة عملاء هيئة الطرق...',
            'example_safety': '⚠️ مخاوف السلامة',
            'example_safety_text': 'تم اكتشاف رائحة غاز بالقرب من محطة أدنوك...',
            'example_inquiry': '❓ استفسار عام',
            'example_inquiry_text': 'ما هي المستندات المطلوبة لتجديد هوية الإمارات...',
        }
    }
    
    # UAE government entity translations
    ENTITY_TRANSLATIONS = {
        'en': {
            'DEWA': 'DEWA',
            'RTA': 'RTA',
            'Etisalat': 'Etisalat',
            'ICA': 'ICA',
            'Tasheel': 'Tasheel',
            'Dubai Police': 'Dubai Police',
            'Abu Dhabi Government': 'Abu Dhabi Government',
        },
        'ar': {
            'DEWA': 'هيئة كهرباء ومياه دبي',
            'RTA': 'هيئة الطرق والمواصلات',
            'Etisalat': 'اتصالات',
            'ICA': 'الهيئة الاتحادية للهوية والجنسية',
            'Tasheel': 'تسهيل',
            'Dubai Police': 'شرطة دبي',
            'Abu Dhabi Government': 'حكومة أبوظبي',
        }
    }
    
    def __init__(self, language='en'):
        self.language = language
    
    def translate(self, key: str) -> str:
        """Translate a key to the current language."""
        return self.TRANSLATIONS.get(self.language, {}).get(key, key)
    
    def translate_entity(self, entity: str) -> str:
        """Translate a government entity name."""
        return self.ENTITY_TRANSLATIONS.get(self.language, {}).get(entity, entity)
    
    def get_bilingual(self, key: str) -> str:
        """Get bilingual text (English/Arabic)."""
        english = self.TRANSLATIONS['en'].get(key, key)
        arabic = self.TRANSLATIONS['ar'].get(key, key)
        return f"{english} / {arabic}"
    
    def set_language(self, language: str):
        """Set the current language."""
        if language in ['en', 'ar']:
            self.language = language
        else:
            self.language = 'en'