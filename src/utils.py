"""
Arabic language utilities for UAE Government System
"""

ARABIC_TRANSLATIONS = {
    # Categories
    "Facilities": "المرافق",
    "Technical / IT": "التقنية / تكنولوجيا المعلومات",
    "Billing": "الفواتير",
    "Inquiry": "الاستفسار",
    "Safety / Emergency": "السلامة / الطوارئ",
    
    # Sentiments
    "Positive": "إيجابي",
    "Neutral": "محايد",
    "Negative": "سلبي",
    
    # Priorities
    "Critical": "حرج",
    "High": "عالي",
    "Medium": "متوسط",
    "Low": "منخفض",
    
    # Departments
    "Emergency Response Center": "مركز الاستجابة للطوارئ",
    "IT Support Division": "قسم الدعم التقني",
    "Finance & Accounts Department": "قسم المالية والمحاسبة",
    "Municipal Services Department": "قسم الخدمات البلدية",
    "Customer Service Center": "مركز خدمة العملاء",
    "Priority Escalation Team": "فريق التصعيد ذات الأولوية",
}

def translate_to_arabic(text: str) -> str:
    """Translate English text to Arabic."""
    return ARABIC_TRANSLATIONS.get(text, text)

def get_bilingual_text(english: str, arabic: str) -> str:
    """Format bilingual text for display."""
    return f"{english} / {arabic}"