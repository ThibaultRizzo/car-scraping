import React from 'react';
import { Table } from 'antd';

const carsData = [{
  id: 1,
  brand: "Volvo",
  price: "1100,23",
  km_number: "12 000"
},
{
  id: 2,
  brand: "Renault",
  price: "1200,23",
  km_number: "12 000"
},
{
  id: 3,
  brand: "Mercedes",
  price: "1000,23",
  km_number: "12 000"
}
];

const columns = [{
  title: '#',
  dataIndex: 'id',
  filters: [{
    text: '1',
    value: '1',
  }],
  onFilter: (value, record) => record.id.indexOf(value) === 0,
  sorter: (a, b) => a.id - b.id,
  sortDirections: ['descend'],
},
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
    <Table columns={columns} dataSource={carsData} onChange={onChange} />);
}

export default TableView;