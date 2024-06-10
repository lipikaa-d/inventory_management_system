from flask import Flask, render_template, request, redirect, url_for, flash
from inventory_model import InventoryModel
from inventory_view import InventoryView


app = Flask(__name__)
app.secret_key = 'lipika'
model = InventoryModel('inventory.csv')

@app.route('/')
def index():
    inventory = model.load_inventory()
    view = InventoryView()
    view.display_inventory(inventory)
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        try:
            item = {
                'item_id': int(request.form['item_id']),
                'name': request.form['name'],
                'quantity': float(request.form['quantity']),
                'issued_to_department': request.form['issued_to_department'].split(','),
                'emp_id': request.form['emp_id'].split(',')
            }
            model.add_item(item)
            flash('Item added successfully.')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(str(e))
    return render_template('add_item.html')

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    item = model.get_item(item_id)
    if not item:
        flash('Item not found.')
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            updated_item = {
                'item_id': item_id,
                'name': request.form['name'],
                'quantity': float(request.form['quantity']),
                'issued_to_department': request.form['issued_to_department'].split(','),
                'emp_id': request.form['emp_id'].split(',')
            }
            model.update_item(item_id, updated_item)
            flash('Item updated successfully.')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(str(e))

    return render_template('update_item.html', item=item)

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    try:
        model.delete_item(item_id)
        flash('Item deleted successfully.')
    except ValueError as e:
        flash(str(e))
    return redirect(url_for('index'))

@app.route('/view/<int:item_id>')
def view_item(item_id):
    print("Received item ID:", item_id)  # Debugging statement
    item = model.get_item(item_id)
    if not item:
        flash('Item not found.')
        return redirect(url_for('index'))
    return render_template('view_item.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)

