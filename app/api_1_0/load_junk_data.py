from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
	jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.models import User, Post, Company, Finance
from app.translate import translate
from app.api_1_0 import bp
import json


def load_company_data():

	c = Company.query.all()

	print("Found companies:")
	print(c)

	company1 = {
		"COMPANY" 		: "Python Software Foundation",
		"COMPANY_CEO"	: "Guido van Rossum",
		"BUSINESS_TYPE"	: "Nonprofit organization"
	}

	company_waynecorp = {
		"COMPANY" 		: "WayneCorp",
		"COMPANY_CEO"	: "Bruce Wayne",
		"BUSINESS_TYPE"	: "Multinational Conglomerate",
	}

	wayne_finance_y1 = {
		"YEAR"				: 2018,
		"Q1_EARNINGS"		: 7825000000.00,
		"Q2_EARNINGS"		: 7825000000.00,
		"Q3_EARNINGS"		: 7825000000.00,
		"Q4_EARNINGS"		: 7825000000.00
	}

	wayne_finance_y2 = {
		"YEAR"				: 2017,
		"Q1_EARNINGS"		: 4321000000.00,
		"Q2_EARNINGS"		: 5412000000.00,
		"Q3_EARNINGS"		: 1255000000.00,
		"Q4_EARNINGS"		: 7622000000.00
	}

	wayne_finance_y3 = {
		"YEAR"				: 2016,
		"Q1_EARNINGS"		: 4443000000.00,
		"Q2_EARNINGS"		: 5412000000.00,
		"Q3_EARNINGS"		: 3125000000.00,
		"Q4_EARNINGS"		: 7622000000.00
	}

	wayne_finance_y4 = {
		"YEAR"				: 2015,
		"Q1_EARNINGS"		: 2511000000.00,
		"Q2_EARNINGS"		: 3345000000.00,
		"Q3_EARNINGS"		: 4556000000.00,
		"Q4_EARNINGS"		: 7001000000.00
	}

	stark_company = {
		"COMPANY" 		: "Stark Industries",
		"COMPANY_CEO"	: "Pepper Potts",
		"BUSINESS_TYPE"	: "Manufacturing",
	}

	stark_finance_y1 = {
		"YEAR"				: 2018,
		"Q1_EARNINGS"		: 7825000000.00,
		"Q2_EARNINGS"		: 7825000000.00,
		"Q3_EARNINGS"		: 7825000000.00,
		"Q4_EARNINGS"		: 7825000000.00
	}

	stark_finance_y2 = {
		"YEAR"				: 2017,
		"Q1_EARNINGS"		: 7825000000.00,
		"Q2_EARNINGS"		: 7825000000.00,
		"Q3_EARNINGS"		: 7825000000.00,
		"Q4_EARNINGS"		: 7825000000.00
	}

	stark_finance_y3 = {
		"YEAR"				: 2016,
		"Q1_EARNINGS"		: 7825000000.00,
		"Q2_EARNINGS"		: 7825000000.00,
		"Q3_EARNINGS"		: 7825000000.00,
		"Q4_EARNINGS"		: 7825000000.00
	}

	stark_finance_y4 = {
		"YEAR"				: 2015,
		"Q1_EARNINGS"		: 7825000000.00,
		"Q2_EARNINGS"		: 7825000000.00,
		"Q3_EARNINGS"		: 7825000000.00,
		"Q4_EARNINGS"		: 7825000000.00
	}

	if c == []:
		print("No companies found!")
		my_company = Company(
			name			= company_waynecorp["COMPANY"],
			company_ceo		= company_waynecorp["COMPANY_CEO"],
			business_type	= company_waynecorp["BUSINESS_TYPE"]
		)
		db.session.add(my_company)

		company1_finance_y1 = Finance(
			year		= wayne_finance_y1["YEAR"],
			q1_earnings	= wayne_finance_y1["Q1_EARNINGS"],
			q2_earnings	= wayne_finance_y1["Q2_EARNINGS"],
			q3_earnings	= wayne_finance_y1["Q3_EARNINGS"],
			q4_earnings	= wayne_finance_y1["Q4_EARNINGS"]
		)
		company1_finance_y2 = Finance(
			year		= wayne_finance_y2["YEAR"],
			q1_earnings	= wayne_finance_y2["Q1_EARNINGS"],
			q2_earnings	= wayne_finance_y2["Q2_EARNINGS"],
			q3_earnings	= wayne_finance_y2["Q3_EARNINGS"],
			q4_earnings	= wayne_finance_y2["Q4_EARNINGS"]
		)
		my_company.finances.append(company1_finance_y1)
		my_company.finances.append(company1_finance_y2)


		stark_finance_y1 = Finance(
			year		= stark_finance_y1["YEAR"],
			q1_earnings	= stark_finance_y1["Q1_EARNINGS"],
			q2_earnings	= stark_finance_y1["Q2_EARNINGS"],
			q3_earnings	= stark_finance_y1["Q3_EARNINGS"],
			q4_earnings	= stark_finance_y1["Q4_EARNINGS"]
		)
		stark_finance_y2 = Finance(
			year		= stark_finance_y2["YEAR"],
			q1_earnings	= stark_finance_y2["Q1_EARNINGS"],
			q2_earnings	= stark_finance_y2["Q2_EARNINGS"],
			q3_earnings	= stark_finance_y2["Q3_EARNINGS"],
			q4_earnings	= stark_finance_y2["Q4_EARNINGS"]
		)
		stark_finance_y3 = Finance(
			year		= stark_finance_y3["YEAR"],
			q1_earnings	= stark_finance_y3["Q1_EARNINGS"],
			q2_earnings	= stark_finance_y3["Q2_EARNINGS"],
			q3_earnings	= stark_finance_y3["Q3_EARNINGS"],
			q4_earnings	= stark_finance_y3["Q4_EARNINGS"]
		)
		stark_finance_y4 = Finance(
			year		= stark_finance_y4["YEAR"],
			q1_earnings	= stark_finance_y4["Q1_EARNINGS"],
			q2_earnings	= stark_finance_y4["Q2_EARNINGS"],
			q3_earnings	= stark_finance_y4["Q3_EARNINGS"],
			q4_earnings	= stark_finance_y4["Q4_EARNINGS"]
		)

		finance_list = [stark_finance_y1, stark_finance_y2, stark_finance_y3, stark_finance_y4]

		my_stark_company = Company(
			name			= stark_company["COMPANY"],
			company_ceo		= stark_company["COMPANY_CEO"],
			business_type	= stark_company["BUSINESS_TYPE"],
			finances		= finance_list
		)
		db.session.add(my_stark_company)
		
		# my_stark_company.finances.append(stark_finance_y1)
		# my_stark_company.finances.append(stark_finance_y2)
		# my_stark_company.finances.append(stark_finance_y3)
		# my_stark_company.finances.append(stark_finance_y4)

		db.session.commit()

	stark_finance_list = [stark_finance_y1, stark_finance_y2, stark_finance_y3, stark_finance_y4]
	stark_company["FINANCE"] = [stark_finance_y1, stark_finance_y2, stark_finance_y3, stark_finance_y4]
	company_waynecorp["FINANCE"] = [wayne_finance_y1, wayne_finance_y2, wayne_finance_y2, wayne_finance_y4]
	print(stark_company)

	with open("Stark_Industries.json", 'w') as json_file:
		json_file.write(json.dumps(stark_company, sort_keys=True, indent=4))

	with open("WayneCorp.json", 'w') as json_file:
		json_file.write(json.dumps(company_waynecorp, sort_keys=True, indent=4))


	return True