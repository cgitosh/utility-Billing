import { Link } from '../../../node_modules/react-router-dom/index';
// material-ui
import { Box, Stack, Typography } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
// third-party
import NumberFormat from 'react-number-format';
import { PlusCircleOutlined } from '@ant-design/icons';

// project import
import Dot from 'components/@extended/Dot';
import { useGetClientsQuery, useGetCategoriesQuery } from './clientsApiSlice';
import MainCard from 'components/MainCard';
// export default function ClientsList() {
const ClientsList = () => {
    // const [clients, setClients] = useState([]);
    const { data: clients = [], isLoading, isSuccess, isError, error } = useGetClientsQuery();
    // const { data: categories = [] } = useGetCategoriesQuery();
    function getFullName(params) {
        return `${params.row.first_name || ''} ${params.row.last_name || ''}`;
    }
    function setFullName(params) {
        const [firstName, lastName] = params.value.toString().split(' ');
        return { ...params.row, firstName, lastName };
    }
    const columns = [
        { field: 'id' },
        { field: 'house_no', headerName: 'House No', editable: false, width: 100 },
        {
            field: 'category',
            headerName: 'Category',
            editable: false,
            width: 200,
            valueGetter: (params) => `${params.row.category.category_name}`
        },
        { field: 'fullName', headerName: 'Client Name', editable: true, width: 150, valueGetter: getFullName, valueSetter: setFullName },
        { field: 'address', headerName: 'Street Address', width: 200 },
        { field: 'mobile_no', headerName: 'Contact No', width: 100 }
    ];
    return (
        <MainCard
            title="Clients List"
            secondary={
                <Stack direction="row" spacing={2} justifyContent="space-between" alignItems="baseline" sx={{ mb: { xs: -0.5, sm: 0.5 } }}>
                    <Link className="btn btn-primary" to="/client/category">
                        Category
                    </Link>
                    <Link className="btn btn-primary" to="/client/create">
                        Client
                    </Link>
                </Stack>
            }
        >
            <div style={{ height: 700, width: '100%' }}>
                <DataGrid
                    rows={clients}
                    columns={columns}
                    pageSize={10}
                    checkboxSelection
                    density="standard"
                    disableSelectionOnClick
                    columnVisibilityModel={{ id: false }}
                />
            </div>
        </MainCard>
    );
};
export default ClientsList;
