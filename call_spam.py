#!/usr/bin/env python3
# call_spam.py - WhatsApp Call Spam
# By Kureza Team

import os
import sys
import time
import random
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

# Konfigurasi
CALL_DELAY_MIN = 3
CALL_DELAY_MAX = 7
MAX_CALLS = 100

def check_termux():
    return os.path.exists("/data/data/com.termux/files/usr")

def call_via_termux(phone_number):
    try:
        number = phone_number.replace('+', '').replace('-', '').replace(' ', '')
        result = subprocess.run(
            ['termux-telephony-call', number],
            capture_output=True,
            timeout=10
        )
        return result.returncode == 0
    except:
        return False

def call_via_android_intent(phone_number):
    try:
        number = phone_number.replace('+', '').replace('-', '').replace(' ', '')
        cmd = f'am start -a android.intent.action.CALL -d tel:{number}'
        result = subprocess.run(cmd, shell=True, capture_output=True, timeout=5)
        return result.returncode == 0
    except:
        return False

def make_call(phone_number):
    if check_termux():
        return call_via_termux(phone_number)
    else:
        return call_via_android_intent(phone_number)

def run_call_spam(phone_number, total_calls, delay_min=3, delay_max=7):
    """Jalankan call spam"""
    print()
    print(f"{Fore.CYAN}┌{'─' * 50}┐{Style.RESET_ALL}")
    print(f"{Fore.CYAN}│{Style.RESET_ALL}  {Fore.GREEN}📞 Memulai Call Spam{Style.RESET_ALL}")
    print(f"{Fore.CYAN}│{Style.RESET_ALL}  {Fore.WHITE}Target   : {Fore.YELLOW}{phone_number}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}│{Style.RESET_ALL}  {Fore.WHITE}Total    : {Fore.YELLOW}{total_calls}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}└{'─' * 50}┘{Style.RESET_ALL}")
    print()
    
    success_count = 0
    fail_count = 0
    
    for i in range(total_calls):
        progress = int((i / total_calls) * 30)
        bar = "█" * progress + "░" * (30 - progress)
        
        result = make_call(phone_number)
        
        if result:
            success_count += 1
            status = f"{Fore.GREEN}✅ Berhasil{Style.RESET_ALL}"
        else:
            fail_count += 1
            status = f"{Fore.RED}❌ Gagal{Style.RESET_ALL}"
        
        print(f"{Fore.CYAN}[{i+1}/{total_calls}] {bar} {int((i/total_calls)*100)}%{Style.RESET_ALL} {status}")
        
        if i < total_calls - 1:
            delay = random.uniform(delay_min, delay_max)
            time.sleep(delay)
    
    print()
    print(f"{Fore.CYAN}╔══════════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.GREEN}📊 HASIL CALL SPAM{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╠══════════════════════════════════════════════════════╣{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.WHITE}✅ Berhasil : {Fore.GREEN}{success_count}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.WHITE}❌ Gagal    : {Fore.RED}{fail_count}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}  {Fore.WHITE}📱 Target   : {Fore.YELLOW}{phone_number}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    return success_count > 0