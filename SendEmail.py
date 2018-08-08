#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

import argparse
import os
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from sys import stdin

# start with - is optional parameter
def getArgs():
    parser = argparse.ArgumentParser()  # Creating a parser
    parser.add_argument('-t','--title',help='The subject of E-mail')
    # parser.add_argument('-s','--start',help='Start Date as YYYY/MM/DD')
    # parser.add_argument('-e','--end',help='End Date as YYYY/MM/DD')
    # parser.add_argument('-m','--mail',help='Send to Email Address, If Not Then output to stdout',default='')
    # parse_args() create an object (argparse.Namespace) holding attributes and return
    # This class is deliberately simple, dict-like view
    args = parser.parse_args()
    return args

# def sendEmail(result,mail):
def sendEmail(title,context):
    # splitted by ,
    strRecipients = "xluo@shancetech.com"
    sender = 'xluo@shancetech.com'
    password = 'xinjianluo_123'
    recipients = strRecipients.split(',')

    # SMTP 只能发送 ASCII 码，而互联网邮件扩充 MIME 可以发送二进制文件。MIME 并没有改动或者取代 SMTP，而是增加邮件主体的结构，定义了非 ASCII 码的编码规则。
    msg = MIMEText(context, 'plain', 'utf-8')  # the body of email
    msg['Subject'] = Header(title, 'utf-8') # the title
    msg['From'] = Header(sender, 'utf-8')
    msg['To'] = Header(strRecipients, 'utf-8')

    # 发送协议常用 SMTP，读取协议常用 POP3 和 IMAP
    SMTPserver = 'smtp.partner.outlook.cn:587'

    try:
        # smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
        mailserver = smtplib.SMTP(SMTPserver)  # SMTP server host


        mailserver.ehlo()
        # Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(sender, password)

        # care of the format of msg (your email, including title, sender, recipient, mail body, etc.), which is defined by SMTP protocol
        mailserver.sendmail(sender, recipients, msg.as_string())
        mailserver.quit()
        print 'Successfully sent a email'
    except smtplib.SMTPException as exp:
        print exp
        print 'Error, cannot send an email'


if __name__== '__main__':
    line=stdin.readline()
    context=line
    while line:
        line=stdin.readline()
        context+=line
    #print context

    args = getArgs()
    if args.title == None:
        print "Need a title! Usage: [-t your_title]"
        exit(0)
    sendEmail(args.title,context)

#sudo /home/xluo/testrundir/shell.sh local | python /home/xluo/PycharmProjects/sendmail/SendEmail.py - t "Automatically TD Latency Testing Log"
