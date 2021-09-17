from selenium.webdriver.support.ui import Select


class AddCustomer:
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    lnkCustomers_MenuItem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddNew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_id = "SearchEmail"
    txtPassword_id = "Password"
    lstAdministrator_id = "AdminComment"
    drpMgrOfVendor_id = "VendorId"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtFirstName_id = "FirstName"
    txtDob_id = "DateOfBirth"
    txtCompany_id = "Company"
    btnSave_xpath = "//button[@name='save']"
    txtLastName_id = "LastName"

    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_MenuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.txtPassword_id).send_keys(password)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_id(self.drpMgrOfVendor_id))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

    def setlastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_id(self.txtDob_id).send_keys(dob)

    def setCompanyname(self, comname):
        self.driver.find_element_by_id(self.txtCompany_id).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.lstAdministrator_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

















