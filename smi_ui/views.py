import numpy as np

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from smi_ui.forms import SignalForm
import wave
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Create your views here.
@csrf_exempt
def signal_page(request):
    if request.method == 'POST':
            # machine learning process!!
            sr, sp = wavfile.read(request.FILES['wav_file'])
            print(sr)
            with wave.open(request.FILES['wav_file'], 'r') as w:
                print(w.readframes(10))
            print(request.FILES['wav_file'])

            modulation = 'FM'
            accuracy = '90%'
            forms = SignalForm()
            return render(request, 'signal/signal.html', locals())

        # return JsonResponse({'is_valid': True, 'a': 2})
    forms = SignalForm()
    return render(request, 'signal/signal.html', locals())
