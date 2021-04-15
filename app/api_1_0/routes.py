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
from app.api_1_0.load_junk_data import load_company_data


@bp.before_app_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()
	g.locale = str(get_locale())


@bp.route('/get_test_results/<int:id>')
@login_required
def get_test_results(id):
	
	if (id < 0): # Add some other testing here:
		message = "Illegal ID value: " + str(id) 
		message = re.sub("<", "", message)
		message = re.sub(">", "", message)

		print(message)


		status_dict = {
			"status": 400,
			"success": False,
			"message": message,
			"contentType":'application/json'
		}
	else:
		message = "Welcome to the API :)"
		status_dict = {
			"status": 200,
			"success": True,
			"message": message,
			"contentType":'application/json'
		}

	data = load_company_data()

	return jsonify(status_dict), 200

@bp.route('/get_company/<int:id>')
@login_required
def get_company(id):
	
	if (id < 0): # Add some other testing here:
		message = "Illegal ID value: " + str(id) 
		message = re.sub("<", "", message)
		message = re.sub(">", "", message)

		print(message)


		status_dict = {
			"status": 400,
			"success": False,
			"message": message,
			"contentType":'application/json'
		}
	else:
		# c = Company.query.filter_by(id=id).first_or_404()
		c = Company.query.filter_by(id=id).first()
		message = "Welcome to the API :)"
		content = {
			"name"			: c.name,
			"ceo_name"		: c.company_ceo,
			"business type"	: c.business_type
		}
		status_dict = {
			"status": 200,
			"success": True,
			"message": message,
			"contentType":'application/json',
			"content": content
		}

	return jsonify(status_dict), status_dict["status"]

@bp.route('/get_finances/<int:id>/<int:year>')
@login_required
def get_finances(id, year):
	
	if (id < 0): # Add some other testing here:
		message = "Illegal ID value: " + str(id) 
		message = re.sub("<", "", message)
		message = re.sub(">", "", message)

		print(message)

		status_dict = {
			"status": 400,
			"success": False,
			"message": message,
			"contentType":'application/json'
		}
		return jsonify(status_dict), status_dict["status"]

	f = Finance.query.filter_by(id=id, year=year).first()
	print(f)
	if f is None:
		# return 500
		message = "No finance records found..."
		status_dict = {
			"status": 404,
			"statusCode": 404,
			"success": False,
			"message": message,
			"error": True,
			"contentType":'application/json'
		}
		return jsonify(status_dict), status_dict["status"]
	# f = Finance.query.filter_by(id=id, year=year).first_or_404()
	message = "Welcome to the API :)"
	content = {
		"year"			: f.year,
		"q1_earnings"	: f.q1_earnings,
		"q2_earnings"	: f.q2_earnings,
		"q3_earnings"	: f.q3_earnings,
		"q4_earnings"	: f.q4_earnings,
	}
	status_dict = {
		"status": 200,
		"success": True,
		"message": message,
		"contentType":'application/json',
		"content": content
	}

	return jsonify(status_dict), status_dict["status"]


# @bp.route('/explore')
# @login_required
# def explore():
#	 page = request.args.get('page', 1, type=int)
#	 posts = Post.query.order_by(Post.timestamp.desc()).paginate(
#		 page, current_app.config['POSTS_PER_PAGE'], False)
#	 next_url = url_for('main.explore', page=posts.next_num) \
#		 if posts.has_next else None
#	 prev_url = url_for('main.explore', page=posts.prev_num) \
#		 if posts.has_prev else None
#	 return render_template('index.html', title=_('Explore'),
#							posts=posts.items, next_url=next_url,
#							prev_url=prev_url)


# @bp.route('/user/<username>')
# @login_required
# def user(username):
#	 user = User.query.filter_by(username=username).first_or_404()
#	 page = request.args.get('page', 1, type=int)
#	 posts = user.posts.order_by(Post.timestamp.desc()).paginate(
#		 page, current_app.config['POSTS_PER_PAGE'], False)
#	 next_url = url_for('main.user', username=user.username,
#						page=posts.next_num) if posts.has_next else None
#	 prev_url = url_for('main.user', username=user.username,
#						page=posts.prev_num) if posts.has_prev else None
#	 return render_template('user.html', user=user, posts=posts.items,
#							next_url=next_url, prev_url=prev_url)


# @bp.route('/edit_profile', methods=['GET', 'POST'])
# @login_required
# def edit_profile():
#	 form = EditProfileForm(current_user.username)
#	 if form.validate_on_submit():
#		 current_user.username = form.username.data
#		 current_user.about_me = form.about_me.data
#		 db.session.commit()
#		 flash(_('Your changes have been saved.'))
#		 return redirect(url_for('main.edit_profile'))
#	 elif request.method == 'GET':
#		 form.username.data = current_user.username
#		 form.about_me.data = current_user.about_me
#	 return render_template('edit_profile.html', title=_('Edit Profile'),
#							form=form)


# @bp.route('/follow/<username>')
# @login_required
# def follow(username):
#	 user = User.query.filter_by(username=username).first()
#	 if user is None:
#		 flash(_('User %(username)s not found.', username=username))
#		 return redirect(url_for('main.index'))
#	 if user == current_user:
#		 flash(_('You cannot follow yourself!'))
#		 return redirect(url_for('main.user', username=username))
#	 current_user.follow(user)
#	 db.session.commit()
#	 flash(_('You are following %(username)s!', username=username))
#	 return redirect(url_for('main.user', username=username))


# @bp.route('/unfollow/<username>')
# @login_required
# def unfollow(username):
#	 user = User.query.filter_by(username=username).first()
#	 if user is None:
#		 flash(_('User %(username)s not found.', username=username))
#		 return redirect(url_for('main.index'))
#	 if user == current_user:
#		 flash(_('You cannot unfollow yourself!'))
#		 return redirect(url_for('main.user', username=username))
#	 current_user.unfollow(user)
#	 db.session.commit()
#	 flash(_('You are not following %(username)s.', username=username))
#	 return redirect(url_for('main.user', username=username))


# @bp.route('/translate', methods=['POST'])
# @login_required
# def translate_text():
#	 return jsonify({'text': translate(request.form['text'],
#									   request.form['source_language'],
#									   request.form['dest_language'])})

