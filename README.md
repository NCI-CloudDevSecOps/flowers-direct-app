
## CI/CD Integrated Cloud Based Flowers Direct Delivery Web App.

### Description
The application named Flowers Direct is an attempt to ease flower delivery process. It acts as interface between the customer(buyer) and flower dealer(seller). The Flowers direct is a cloud based web application developed using Django Framework and Python 3.9 which provides customers to view and select the flowers they wish to order.

### Technologies Used
- Python 3
- Django Framework
- SQLite3 Database
- HTML5
- Bootstrap5

### Setup Instructions
1. Clone the repository: `git clone https://github.com/NCI-CloudDevSecOps/flowers-direct-app.git`
2. Navigate to the project directory: `cd flowers-direct-app`
3. Install dependencies using `pip` and the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
6. Access the application at `http://localhost:8080` in your web browser.

### Project Structure
- **/flowersdirect**: Contains the Django application files.
- **/flowersdirect**: Contains the project settings and configurations.
- **/static**: Directory for static files (CSS, JavaScript, etc.).
- **/templates**: Directory for HTML templates.
- **requirements.txt**: Lists all Python dependencies for the project.
- **buildspec.yml**: AWS CodeBuild build specification file.
- **sonar-spec.yml**: Sonar review configuration file.

### Additional Notes
Seller login creds : 
username:seller
Password: Password@1

---

If you have any questions or need further assistance, please don't hesitate to ask!
