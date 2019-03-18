/** Configuration constants **/
export const BASE_URL = function getBaseUrl() {
    if (process.env.NODE_ENV === 'development') {
        return 'http://127.0.0.1:8000';
    } else if (process.env.NODE_ENV === 'production') {
        return 'https://team-pack-dev.herokuapp.com';
    }
}();
export const NUMBERS_URL = BASE_URL + '/carstat/numbers/';
export const TREEMAP_URL = BASE_URL + '/carstat/treemaps/';
export const BOXPLOT_URL = BASE_URL + '/carstat/boxplot/';
export const PAGINATED_CARS_URL = BASE_URL + '/api/cars/recent_cars/?page=';
export const SCRAPING_URL = BASE_URL + '/api/scrap/';
export const CAR_CSV_URL = BASE_URL + '/api/cars/get_car_csv/';

/** Display constants **/
export const TREEMAP_VENDOR_LIST = ['aramisAuto', 'lacentrale', 'goodbuyauto.it'];
export const CAR_LABEL_DICT = {
    "vendor_ref": "Vendor Reference",
    "price": "Price",
    "km_number": "Kilometers",
    "brand": "Brand",
    "model": "Model",
    "car_type": "Car Type",
    "vendor": "Vendor",
    "reg_date": "Registration Date",
    "gear_box": "Gear Box",
    "gear_number": "Gear number",
    "motor_type": "Motor Type",
    "petrol_type": "Petrol Type",
    "color": "Color",
    "doors_number": "Door Number",
    "vendor_link": "Link to Vendor",
    "owner_number": "Owner Number",
    "reg_number": "Registration Number"
};