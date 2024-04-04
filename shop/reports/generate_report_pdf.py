from reportlab.pdfgen import canvas
from io import BytesIO
from order.models import Order


def generate_pdf_report(orders, data_parameters):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    param_mapping = {
        "order.id": "Order ID",
        "order.buyer": "Order Buyer",
        "order.street": "Order Street",
        "order.city": "Order City",
        "order.postcode": "Order Postcode",
        "order.date": "Order Date",
        "order.delivery.name": "Order Delivery Name",
        "order.delivery.price": "Order Delivery Price",
        "order.status": "Order Status",
    }

    y_position = 800

    for order in orders:
        for param in data_parameters:
            if param in param_mapping:
                if param == "order.delivery.name":
                    pdf.drawString(
                        100,
                        y_position,
                        f"{param_mapping[param]}: {order.delivery.name}",
                    )
                elif param == "order.delivery.price":
                    pdf.drawString(
                        100,
                        y_position,
                        f"{param_mapping[param]}: {order.delivery.price}",
                    )
                else:
                    pdf.drawString(
                        100,
                        y_position,
                        f"{param_mapping[param]}: {getattr(order, param.split('.')[1])}",
                    )
                y_position -= 20

        y_position -= 20

    pdf.save()
    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data


def filter_orders_by_date(start_date, end_date, user_id):
    orders = Order.objects.filter(date__range=(start_date, end_date), buyer=user_id)
    return orders
