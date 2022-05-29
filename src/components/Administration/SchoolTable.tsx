import { DataGrid, GridColDef, GridValueGetterParams, GridRenderCellParams } from '@mui/x-data-grid';
import Button from '@mui/material/Button';
import {
  Link
} from "react-router-dom";

const columns: GridColDef[] = [
  {
    field: 'id',
    headerName: 'ID',
    width: 90,
    renderCell: (params) => { return <Link to={`/SchoolTable/${params.value}`}>{params.value}</Link> }

  },

  {
    field: 'name',
    headerName: 'Наименование',
    width: 150,
    editable: true,
  },

  {
    field: 'adress',
    headerName: 'Адрес',
    width: 250,
    editable: true,
    valueGetter: (params: GridValueGetterParams) =>
      `${params.row.id || ''} ${params.row.name || ''}`,
  }

];

const rows = [
  { id: 1, name: 'Snow', adress: 'Jon' },
  { id: 2, name: 'Lannister', adress: 'Cersei' },
  { id: 3, name: 'Lannister', adress: 'Jaime' },
];


export default function SchoolEditing() {
  return (
    <div style={{ height: 400, width: '100%' }}>

      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <h3> Школы </h3>
      </div>

      <div style={{ border: 10, borderBottomWidth: 10, borderColor: "HighlightText" }}>
        <Button variant="contained" style={{ marginLeft: 5 }} component={Link} to={"/SchoolTable/-1"}> Добавить</Button>
      </div>

      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        disableSelectionOnClick
      />

    </div>
  );
}
