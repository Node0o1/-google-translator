from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from languages import supported_languages

def help_handle():
    print('Sending help message\n')
    return '```!Google Translate-bot Help Message\n\nMESSAGE FORMAT:\n?language-to-translate-to message-to-translate\n\nEXAMPLE:\n?spanish good morning everyone\n\nNOTE:\nFor language support type "?langs"```'

def list_language_handle():
    print('Sending supported language list\n')
    lang_list='```SUPPORTED supported_languages:\n'
    for key, value in supported_languages.items():
        lang_list+=(key+', ')
    lang_list+='```'
    return lang_list

def check_supported_language_handle(message):
    is_in=False
    lang=str(message).split(" ")[0][1:]
    message=str(message).strip('?'+lang)
    lang=lang.lower()
    while(not is_in):
        try:
            if supported_languages[lang]:
                is_in = True
                translation_lang=supported_languages[lang]
                print(f'TRANSLATE TO: {lang.upper()}{chr(0x0a)}LANGUAGE CODE: {translation_lang}')
        except:
            print(f'Unsupported language request({lang})')
            return (f'Language {lang} not found.')
        else:
            return translate_handle(message, translation_lang, lang)

def translate_handle(message, translation_lang, lang):
    try:
        url_string=quote(message)
        url=f'https://translate.google.com/?sl=auto&tl={translation_lang}&text={url_string}&op=translate'
        options=Options()
        options.add_argument("--headless")
        options.page_load_strategy='normal'
        driver=webdriver.Firefox(options=options)
        driver.get(url)
        time.sleep(2)#allow load to fully finish

        native_lang=driver.find_element(By.CLASS_NAME,"zXU7Rb")
        try:
            translations=driver.find_elements(By.CLASS_NAME, "lRu31")
            if(len(translations)>1):
                translation=translations[1].text.strip('(masculine)')
            else:
                translation=translations[0].text
        except:
            translation=driver.find_element(By.CLASS_NAME, "lRu31").text

        print(f'DETECTED LANGUAGE: {native_lang.text.split(" ")[0]}')
        print(f'TRANSLATION: {translation}{chr(0x0a)}')
       
        return_phrase=f'DETECTED LANGUAGE: {native_lang.text.split(" ")[0]}{chr(0X0A)}{lang.upper()} TRANSLATION: {translation}'
        driver.quit()
        return return_phrase
    
    except Exception as e:
        err='Translation Error: scrape incomplete'
        print(e)
        print(err+chr(0x0a))
        return err
    
