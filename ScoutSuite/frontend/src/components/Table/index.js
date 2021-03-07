import React from 'react';
import { PropTypes } from 'prop-types';

import TableRender from './Renderer/index';

import './style.scss';

const propTypes = {
  columns: PropTypes.arrayOf(PropTypes.object).isRequired,
  data: PropTypes.arrayOf(PropTypes.object).isRequired,
  initialState: PropTypes.object,
  formatters: PropTypes.object,
  sortBy: PropTypes.object,
};

const Table = (props) => {
  const {
    columns,
    data,
    initialState = {},
    formatters = {},
    sortBy = {},
  } = props;

  const cols = columns.map((item) => {
    let col = {
      Header: item.name,
      accessor: item.key,
      ...item,
    };
    if (formatters[item.key]) col.Cell = formatters[item.key];
    if (sortBy[item.key]) col.sortType = sortBy[item.key];
    return col;
  });

  return (
    <TableRender
      columns={cols}
      data={data}
      initialState={initialState}
      hasPagination={!!initialState.pageCount}
    />
  );
};

Table.propTypes = propTypes;

export default Table;