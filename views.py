import datetime
import io
import sqlite3
import json
import boto3
import pandas
from django.shortcuts import render
from datetime import  timedelta, date

from django.shortcuts import render
import  pandas as pd
import snowflake as sn
# Create your views here.
from django.views.decorators.cache import cache_page

from snowflaketest.models import student

con = sqlite3.connect(r"C:\Users\Nayana Nandakumar\Docker\jenkinsprojectnew1\snowflakes\db.sqlite3")
# username = 'nayannandakumar'
# password = 'Idontknow@1'
# account = 'vd04846.ap-south-1'
# warehouse = 'COMPUTE_WH'
# database = 'TESTDB'
# ctx = sn.connector.connect(
#     user=username,
#     password=password,
#     account=account,
#     # warehouse=warehouse,
#     database=database,
#     schema='PUBLIC'
# )
# # con=sqlite3.connect("db.sqlite3")
# # print(con)
# # df=pd.read_sql_query("SELECT * from student",con)
# # print(df.head())
from snowflake import connector
from snowflaketest.forms import studentfrom
username = 'nayannandakumar'
password = 'Idontknow@1'
account = 'vd04846.ap-south-1'
warehouse = 'COMPUTE_WH'
database = 'TESTDB'
ctx = sn.connector.connect(
    user=username,
    password=password,
    account=account,
    # warehouse=warehouse,
    database=database,
    schema='PUBLIC'
)


def stuent(request):

    form = studentfrom(request.POST)
    if form.is_valid():
        form.save()
    else:
        print("not working")

    return render(request,'studentform.html',{'form':form})


def datatable(request):
    number = request.POST.get("select")
    print(number)
    if number == "1" :
        cs = ctx.cursor()
        cs.execute("USE WAREHOUSE MEDIUMHOUSE")
        cs.execute("select * from x where T >= dateadd(month, -3, current_date)")
        df = cs.fetchall()
        return render(request, 'table.html',{"query" : df} )
    elif number =="2":

        startdate = date.today()
        employees = student.objects.raw("select * from student where CREATED_AT >=  DATE('now', '-2 MONTH')")
        return render(request, 'table.html', {"employees": employees})
    elif number == "3":
        client = boto3.client(
            "s3",
            aws_access_key_id="AKIAZHLJO7N5SSKSIXV5",
            aws_secret_access_key="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",
            region_name="us-east-2"

        )

        clientResponse = client.list_buckets()

        # Print the bucket names one by one
        print('Printing bucket names...')
        # for bucket in clientResponse['Buckets']:
        #     print(f'Bucket Name: {bucket["Name"]}')

        obj = client.get_object(
            Bucket='bhavdatabucket',
            Key='bhavdata.xls'
        )

        # Read data from the S3 object
        data = pandas.read_excel(io.BytesIO(obj['Body'].read()))
        # Print the data frame
        json_records = data.reset_index().to_json(orient='records')
        data = json.loads(json_records)
        #
        # print('Printing the data frame...')
        # print(data)
        return render(request, 'table.html', {"data": data})
    else :
        print("not worling")
    return render(request, 'table.html',)



