from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer, PengaduanSerializer
from .forms import WargaForm, PengaduanForm
from rest_framework import viewsets
from .serializers import WargaSerializer

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class WargaUpdateView(UpdateView):
    model = Warga
    fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    from_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url =reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm # <--- INI BENAR
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('warga-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class PengaduanListAPIView(ListAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer

class PengaduanDetailAPIView(RetrieveAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer

class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer

# Create your views here.
