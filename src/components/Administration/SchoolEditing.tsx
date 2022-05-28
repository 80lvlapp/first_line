import { DataGrid, GridColDef, GridValueGetterParams } from '@mui/x-data-grid';

const columns: GridColDef[] = [
  { field: 'id', headerName: 'ID', width: 90 },
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
  { id: 2, name: 'Lannister', adress: 'Cersei'},
  { id: 3, name: 'Lannister', adress: 'Jaime'},
];


export default function SchoolEditing() {
  return (
    <div style={{ height: 400, width: '100%' }}>

      <h5>Школы</h5>

      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
        disableSelectionOnClick
      />

    </div>
  );
}
