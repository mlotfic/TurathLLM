# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 13:27:48 2025

@author: m
"""



import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

import re
import unicodedata
import numpy as np

from pyarabic import araby
from pyarabic.araby import strip_tatweel
from pyarabic.number import detect_number_phrases_position, text2number

def safe_text2number(text: str) -> str:
    """
    Safely convert Arabic text numbers to digits
    
    Args:
        text (str): Input text potentially containing number words
    
    Returns:
        str: Text with number phrases converted to digits
    """
    if not text or len(text.strip()) < 2:
        return text
    
    try:
        wordlist = araby.tokenize(text)
        positions_phrases = detect_number_phrases_position(wordlist)
        
        if not positions_phrases:
            return text
        
        modified_wordlist = wordlist.copy()
        
        for start, end in positions_phrases:
            number_phrase = ' '.join(wordlist[start:end+1])
            
            try:
                converted_number = str(text2number(number_phrase))
                modified_wordlist[start] = converted_number
                modified_wordlist[start+1:end+1] = [''] * (end - start)
            except Exception as e:
                logger.warning(f"Number conversion failed: {e}")
                continue
        
        final_text = ' '.join(str(word) for word in modified_wordlist if word)
        return final_text
    
    except Exception as e:
        logger.error(f"Text to number conversion error: {e}")
        return text

def normalize_arabic(
    text: str, 
    advanced_normalization: bool = True, 
    preserve_numbers: bool = True
) -> str:
    """
    Advanced Arabic text normalization function
    
    Args:
        text (str): Input Arabic text to be normalized
        advanced_normalization (bool): Enable advanced normalization techniques
        preserve_numbers (bool): Preserve English/Arabic numbers
    
    Returns:
        str: Normalized Arabic text
    """
    try:
        # Ensure input is a string
        text = str(text)
        
        # Convert number words
        text = safe_text2number(text)
        
        # Normalization mapping
        normalization_map = {
            'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 
            'ٱ': 'ا', 
            'ى': 'ي', 
            'ة': 'ه',
            'ؤ': 'و',
            'ئ': 'ي'
        }
        
        # Apply character normalization
        for char, replacement in normalization_map.items():
            text = text.replace(char, replacement)
        
        # Lowercase and clean
        text = text.lower()
        text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # Remove URLs
        text = re.sub(r'\S+@\S+', '', text)  # Remove email addresses
        
        # Remove diacritics
        text = re.sub(r'[\u064B-\u0652]', '', text)
        text = strip_tatweel(text)
        
        # Advanced normalization
        if advanced_normalization:
            # Normalize Arabic numerals
            arabic_numerals = {
                '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
                '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
            }
            
            text = re.sub(r'[٠-٩]', 
                          lambda m: arabic_numerals.get(m.group(0), m.group(0)), 
                          text)
            
            # Additional cleaning
            text = re.sub(r'(.)\1{2,}', r'\1', text)  # Remove repeated chars
            
            # Normalize punctuation
            replacements = {
                '،': ',', '؛': ';', '؟': '?'
            }
            for ar, en in replacements.items():
                text = text.replace(ar, en)
            
            # Character preservation
            if not preserve_numbers:
                text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
            else:
                text = re.sub(r'[^\u0600-\u06FF\s0-9.,;:!?]', '', text)
        
        # Final cleanup
        text = re.sub(r'(\s)\1+', r'\1', text).strip()
        
        return text
    
    except Exception as e:
        logger.error(f"Arabic normalization error: {e}")
        return text