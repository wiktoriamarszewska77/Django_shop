from reportlab.pdfgen import canvas
from io import BytesIO


def generate_payment_report(order):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    pdf.drawString(100, 800, f"Payment Report for Order ID: {order.id}")
    pdf.drawString(100, 780, f"Buyer: {order.buyer}")
    pdf.drawString(100, 760, f"Street: {order.street}")
    pdf.drawString(100, 740, f"City: {order.city}")
    pdf.drawString(100, 720, f"Postcode: {order.postcode}")
    pdf.drawString(100, 700, f"Date: {order.date}")
    pdf.drawString(100, 680, f"Delivery: {order.delivery.name}")
    pdf.drawString(100, 660, f"Delivery price: {order.delivery.price}")
    pdf.drawString(100, 640, f"Status: {order.status}")
    pdf.drawString(100, 620, "-" * 50)

    pdf.save()
    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data
