import smtplib

my_email = "your mail"
my_pass = "your auth key"


def shoot_mail(file_url, name,email,phoneno,filename):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject: {filename} | DeepTumor Cancer Detection Report\n\n"
                                f"Dear {name},\n"
                                f"Patient ID: {filename}\n"
                                f"Phone No: {phoneno}\n"
                                f"Thank you for using DeepTumor for your cancer detection. We are pleased to inform you that your cancer test results are ready.\n"
                                f"Attached to this email, you will find your detailed cancer detection report url. Please take a moment to review the report and let us know if you have any questions or concerns.\n"
                                f"We understand that a cancer diagnosis can be difficult to process, and we want to assure you that we are here to support you throughout your journey. If you require further assistance or guidance, please do not hesitate to contact us.\n"
                                f"Thank you for choosing DeepTumor for your healthcare needs.\n"
                                f"Best regards,\n"
                                f"DeepTumor Team\n\n\n"
                                f"Report Link: {file_url}"

                            )

        print("Message sent")
