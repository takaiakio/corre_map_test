import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from .forms import UploadFileForm

def handle_uploaded_file(f):
    df = pd.read_csv(f)
    return df

def correlation_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            df = handle_uploaded_file(request.FILES['file'])
            correlation = df.corr()
            plt.figure()
            plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
            plt.xlabel(df.columns[0])
            plt.ylabel(df.columns[1])
            plt.title('Correlation: {:.2f}'.format(correlation.iloc[0, 1]))
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            return render(request, 'analysis/result.html', {'form': form, 'image_base64': image_base64})
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
