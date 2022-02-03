import creditcard_validation
import pytest

def test_method():
     
    assert creditcard_validationObject.valid_sum("378282246310005")==True
    # test for invalid number
    assert creditcard_validationObject.valid_sum("378282246310075")==False
    assert creditcard_validation7Object.valid_starting("45")==False
    # invalid  CVV
    assert creditcard_validationObject.valid_cv(12)==False
    assert creditcard_validationObject.valid_cv(1989892)==False
    # correct CVV
    assert creditcard_validationObject.valid_cv(123)==True
    # invalid date
    assert creditcard_validationObject.valid_date(14/09/2020)==False
    # valid date
    assert creditcard_validationObject.valid_date("14/09/2022")==true
    
