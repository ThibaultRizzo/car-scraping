import React from 'react';
import { Table } from 'antd';

// const ex = {
//   "vendor_ref": "rv334806",
//   "price": "11890.00",
//   "km_number": 103183,
//   "brand": "Peugeot",
//   "model": "508 SW",
//   "car_type": "Allure",
//   "vendor": "Aramisauto",
//   "reg_date": null,
//   "gear_box": "Boîte manuelle",
//   "gear_number": "6 rapports",
//   "motor_type": "2.0 HDi 140 BVM6",
//   "petrol_type": "Diesel",
//   "color": null,
//   "doors_number": "5 portes",
//   "vendor_link": "https://www.aramisauto.com/voitures/peugeot/508-sw/allure/rv334806",
//   "owner_number": null,
//   "reg_number": null
// }

const columns = [
  {
    title: 'Ref',
    dataIndex: 'vendor_ref'
  },
  // {
  //   title: '#',
  //   dataIndex: 'id',
  //   filters: [{
  //     text: '1',
  //     value: '1',
  //   }],
  //   onFilter: (value, record) => record.id.indexOf(value) === 0,
  //   sorter: (a, b) => a.id - b.id,
  //   sortDirections: ['descend'],
  // },
  {
    title: 'Price',
    dataIndex: 'price',
    sorter: (a, b) => a.price - b.price,
    sortDirections: ['descend'],
  },
  {
    title: 'Brand',
    dataIndex: 'brand',
    sorter: (a, b) => a.brand.length - b.brand.length,
    sortDirections: ['descend', 'ascend'],
  },
  {
    title: 'Kilometers',
    dataIndex: 'km_number',
    sorter: (a, b) => a.km_number.length - b.km_number.length,
    sortDirections: ['descend', 'ascend'],
  }]

function onChange(pagination, filters, sorter) {
  console.log('params', pagination, filters, sorter);
}

const TableView = (props) => {
  return (
    <Table columns={columns} dataSource={props.data} onChange={onChange} />);
}

export default TableView;