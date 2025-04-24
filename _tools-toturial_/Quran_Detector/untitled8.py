# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:44:22 2025

@author: m
"""

from QuranDetectorAnnotater import qMatcherAnnotater,term
import codecs

qAn = qMatcherAnnotater()

# Code to read in the test tweets and to generate the tool output 
def outPutResults(fname, outF):
    f = codecs.open(fname, "r", "utf-8")
    f2 = codecs.open(outF, "w", "utf-8")
    i =1 
    for line in f:
        sp = line.split('\t')
        if len(sp)!= 2:
            print('err in line', i)
            continue
        idd = sp[0]
        tweet = sp[1].strip()
        #print(tweet)
        v_matches = qAn.matchAll(tweet,allowedErrPers=0.2 )
        matches = []
        unique = set([])
        for i in range(len(v_matches)): 
            r1 = v_matches[i]
            aya = r1['aya_name'] + ':' 
            if (r1['aya_start']) != (r1['aya_end']):
                aya = aya + str(r1['aya_start']) + '-' + str((r1['aya_end']))
            else:
                aya = aya + str(r1['aya_start'])

            start = int(r1['startInText'])
            end = int(r1['endInText'])
            loc = (start,end)
            unique.add(loc)
            m = tweet.split()[start:end]
            matches.append((' '.join(m),aya))
        f2.write(idd + "\t" + str(matches)+  "\t" +str(len(unique))+ "\n")
        i= i+1
        
    f.close()
    f2.close()
    
#Calling matchAll without changing any of the values of the default parmaters 
txt = "RT @user: كرامة المؤمن عند الله تعالى؛ حيث سخر له الملائكة يستغفرون له ﴿الذِين يحملونَ العرشَ ومَن حَولهُ يُسبحو بِحمدِ ربهِم واذكر ربك إذا نسيت…"  
vs = qAn.matchAll(txt)
print(vs)
print(len(vs), 'entrie(s) returned.' )

#Another example
txt = 'RT @user: بسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ  قُلْ هُوَ اللَّهُ أَحَدٌ ۞ اللَّهُ الصَّمَدُ ۞ لَمْ يَلِدْ وَلَمْ يُولَدْ ۞ وَلَمْ يَ…'
vs = qAn.matchAll(txt)
print(vs)
print(len(vs), 'entrie(s) returned.' )

#an example where a missing word is detected
txt = 'الم ذلك الكتاب لا ريب هدي للمتقين'
vs = qAn.matchAll(txt)
print(vs)
print(len(vs), 'entrie(s) returned.' )


txt = 'RT @HolyQraan: من قرأها ثلاث مرات فكأنما قرأ القرآن كاملا ..   ﴿قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ ۝ لَمْ يَلِدْ وَلَمْ يُولَدْ…'
vs = qAn.matchAll(txt)
print(vs)
print(len(vs), 'entrie(s) returned.' )

# here we remove الله from the first verse
# the missing word appears in the error list of the first verse. 
txt = 'RT @HolyQraan: من قرأها ثلاث مرات فكأنما قرأ القرآن كاملا ..   ﴿قُلْ هُوَ أَحَدٌ ۝ اللَّهُ الصَّمَدُ ۝ لَمْ يَلِدْ وَلَمْ يُولَدْ…'
vs = qAn.matchAll(txt)
print(vs)
print(len(vs), 'entrie(s) returned.' )


#now we dis-able the detection of missing words. Again, the verse where a missing word exists, is now no longer detected. 
txt = 'RT @HolyQraan: من قرأها ثلاث مرات فكأنما قرأ القرآن كاملا ..   ﴿قُلْ هُوَ أَحَدٌ ۝ اللَّهُ الصَّمَدُ ۝ لَمْ يَلِدْ وَلَمْ يُولَدْ…'
vs = qAn.matchAll(txt, findMissing=False)
print(vs)


#In this example we increase the error tolerance. This is not advised because you might end up with matches that are not accurate

#With the default error tolerance of 25% or 0.25
txt = 'RT @HolyQraan: من قرأها ثلاث مرات فكأنما قرأ القرآن كاملا ..   ﴿قُلْ هُوَا اللَّهُ أَحَ…'
print('With the default error tolerance of 25% or 0.25 (no matches returned):')
vs = qAn.matchAll(txt)
print(vs)

#With the increaced error tolerance
vs = qAn.matchAll(txt, allowedErrPers=0.5)
print('With the increaced error tolerance:')
print(vs)

## Annotating Text
txt = "RT @user:... كرامة المؤمن عند الله تعالى؛ حيث سخر له الملائكة يستغفرون له ﴿الذِين يحملونَ العرشَ ومَن حَولهُ يُسبحونَ بِحمدِ ربهِم…"
t = qAn.annotateTxt(txt)
print('')
print(t)

#note how the last word has been automatically corrected 
txt = ' واستعينوا بالصبر والصلاه وانها لكبيره الا علي الخشعين'
qAn.annotateTxt(txt)

txt = 'RT @7Life4ever: ﷽  قل هو ﷲ أحد۝ ﷲ الصمد۝لم يلد ولم يولد۝ولم يكن له كفوا أحد  ﷽  قل أعوذ برب الفلق۝من شر ما خلق ۝ومن شر غاسق إذا وقب۝ومن شر ا…'
qAn.annotateTxt(txt)


txt = '''
# اعلم يا أخي أن الله تعالى فضل مكة على سائر البلاد وأنزل ذكرها في كتابه
~~العزيز في مواضع عديدة فقال تعالى {إن أول بيت وضع للناس للذي ببكة مباركا
~~وهدى للعالمين فيه آيات بينات مقام إبراهيم ومن دخله كان آمنا}

'''
txt = txt.replace("~~", "")
t = qAn.annotateTxt(txt)
qAn.annotateTxt(txt)
vs = qAn.matchAll(txt)
print(vs)
print(len(vs), 'entrie(s) returned.' )
