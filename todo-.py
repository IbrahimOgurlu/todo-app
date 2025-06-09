from fpdf import FPDF
import datetime


musteri_adi = input("Müşteri adı: ")
urun = input("Ürün adı: ")
adet = int(input("Adet: "))
fiyat = float(input("Birim fiyat (₺): "))
tarih = datetime.datetime.today().strftime('%d/%m/%Y')


toplam = adet * fiyat


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="FATURA", ln=True, align='C')
pdf.ln(10)
pdf.cell(100, 10, txt=f"Tarih: {tarih}", ln=True)
pdf.cell(100, 10, txt=f"Müşteri: {musteri_adi}", ln=True)
pdf.cell(100, 10, txt=f"Ürün: {urun}", ln=True)
pdf.cell(100, 10, txt=f"Adet: {adet}", ln=True)
pdf.cell(100, 10, txt=f"Birim Fiyat: {fiyat} ₺", ln=True)
pdf.cell(100, 10, txt=f"Toplam: {toplam} ₺", ln=True)

pdf.output("fatura.pdf")

print("✅ Fatura başarıyla oluşturuldu: fatura.pdf")