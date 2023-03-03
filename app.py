from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2  # pip install psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

# DB_HOST = "127.0.0.1"
# DB_NAME = "postgres"
# DB_USER = "postgres"
# DB_PASS = "2708"

DB_HOST = "john.db.elephantsql.com"
DB_NAME = "phtolxap"
DB_USER = "phtolxap"
DB_PASS = "YyTGeL70QsUQx0psxtztK0kvadm-FnyH"

conn = psycopg2.connect(user=DB_USER, password=DB_PASS,
                        host=DB_HOST, database=DB_NAME)


@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM householdid"
    cur.execute(s)  # Execute the SQL
    list_users = cur.fetchall()
    return render_template('./index.html', list_users=list_users)


@app.route('/admin')
def admin():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM householdid"
    cur.execute(s)  # Execute the SQL
    list_users = cur.fetchall()
    return render_template('./admin.html', list_users=list_users)


@app.route('/add_household', methods=['POST'])
def add_household():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        if request.method == 'POST':

            print("hhid", request.form['hhid'])
            print("lat", request.form['lat'])
            print("long", request.form['long'])
            print("hhmem", request.form['hhmem'])
            print("mfratio", request.form['mfratio'])
            print("working", request.form['working'])
            print("migrated", request.form['migrated'])
            print("occu", request.form['occu'])
            print("amount", request.form['amount'])
            print("edu", request.form['edu'])
            print("max_edu", request.form['max_edu'])
            print("land_hold", request.form['land_hold'])
            print("house_type", request.form['house_type'])
            print("toilet_fac", request.form['toilet_fac'])
            print("electricity", request.form['electricity'])
            print("money_house", request.form['money_house'])
            print("extended_damage", request.form['extended_damage'])
            print("loan", request.form['loan'])
            print("crop_loss", request.form['crop_loss'])
            print("annu_income", request.form['annu_income'])

            hhid = request.form['hhid']
            lat = request.form['lat']
            long = request.form['long']
            hhmem = request.form['hhmem']
            mfratio = request.form['mfratio']
            working = request.form['working']
            migrated = request.form['migrated']
            occu = request.form['occu']
            amount = request.form['amount']
            edu = request.form['edu']
            max_edu = request.form['max_edu']
            land_hold = request.form['land_hold']
            house_type = request.form['house_type']
            toilet_fac = request.form['toilet_fac']
            electricity = request.form['electricity']
            money_house = request.form['money_house']
            extended_damage = request.form['extended_damage']
            loan = request.form['loan']
            crop_loss = request.form['crop_loss']
            annu_income = request.form['annu_income']

            cur.execute("INSERT INTO householdid (hhid, lat, long,hhmem,mfratio,working,migrated,occu,amount,edu,max_edu,land_hold, house_type,toilet_fac,electricity,money_house,extended_damage,loan,crop_loss,annu_income) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (hhid, lat, long, hhmem, mfratio, working, migrated, occu, amount, edu, max_edu, land_hold, house_type, toilet_fac, electricity, money_house, extended_damage, loan, crop_loss, annu_income))
            conn.commit()
            flash('household Added successfully')
            return redirect(url_for('admin'))
    except Exception as e:
        print(e)
        return "There was an issue adding your household"


@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_employee(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM householdid WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    # print(data[0])
    return render_template('edit.html', household=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_household(id):
    if request.method == 'POST':
        hhid = request.form['hhid']
        lat = request.form['lat']
        long = request.form['long']
        hhmem = request.form['hhmem']
        mfratio = request.form['mfratio']
        working = request.form['working']
        migrated = request.form['migrated']
        occu = request.form['occu']
        amount = request.form['amount']
        edu = request.form['edu']
        max_edu = request.form['max_edu']
        land_hold = request.form['land_hold']
        house_type = request.form['house_type']
        toilet_fac = request.form['toilet_fac']
        electricity = request.form['electricity']
        money_house = request.form['money_house']
        extended_damage = request.form['extended_damage']
        loan = request.form['loan']
        crop_loss = request.form['crop_loss']
        annu_income = request.form['annu_income']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE householdid
            SET hhid = %s
              lat = %s
              long = %s
              hhmem = %s
              mfratio = %s
              working = %s
              migrated = %s
              occu = %s
              amount = %s
              edu = %s
              max_edu = %s
              land_hold= %s
              house_type = %s
              toilet_fac = %s
              electricity= %s
              money_house = %s
              extended_damage = %s
              loan = %s
              crop_loss = %s
              annu_income = %s
            WHERE id = %s
        """, (hhid, lat, long, hhmem, mfratio, working, migrated, occu, amount, edu, max_edu, land_hold, house_type, toilet_fac, electricity, money_house, extended_damage, loan, crop_loss, annu_income, id))
        flash('household Updated Successfully')
        conn.commit()
        return redirect(url_for('admin'))


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_household(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DELETE FROM householdid WHERE id = {0}'.format(id))
    conn.commit()
    flash('household Removed Successfully')
    return redirect(url_for('admin'))


if __name__ == "__main__":
    app.run(debug=True)
