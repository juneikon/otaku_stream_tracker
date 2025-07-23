from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Anime
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    anime_list = Anime.query.all()
    return render_template('index.html', anime_list=anime_list)

@main.route('/add', methods=['GET', 'POST'])
def add_anime():
    if request.method == 'POST':
        title = request.form['title']
        status = request.form['status']
        if title:
            new_anime = Anime(title=title, status=status)
            db.session.add(new_anime)
            db.session.commit()
            flash('Anime added!')
            return redirect(url_for('main.index'))
    return render_template('add_anime.html')

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update_anime(id):
    anime = Anime.query.get_or_404(id)
    if request.method == 'POST':
        anime.title = request.form['title']
        anime.status = request.form['status']
        db.session.commit()
        flash('Anime updated!')
        return redirect(url_for('main.index'))
    return render_template('update_anime.html', anime=anime)

@main.route('/delete/<int:id>')
def delete_anime(id):
    anime = Anime.query.get_or_404(id)
    db.session.delete(anime)
    db.session.commit()
    flash('Anime deleted!')
    return redirect(url_for('main.index'))
