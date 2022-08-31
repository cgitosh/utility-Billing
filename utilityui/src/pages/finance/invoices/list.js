import { Link } from 'react-router-dom';
// material-ui
import { Box, Stack, Typography } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
// third-party
import NumberFormat from 'react-number-format';
import { PlusCircleOutlined } from '@ant-design/icons';

// project import
import Dot from 'components/@extended/Dot';
import { useGetInvoicesQuery, useGetInvoiceQuery } from './invoiceApiSlice';
import MainCard from 'components/MainCard';
const InvoiceList = () => {
    // const [clients, setClients] = useState([]);
    const { data: invoices = [], isLoading, isSuccess, isError, error } = useGetInvoicesQuery();
    // const { data: clients, isLoading, isSuccess, isError, error } = useGetClientsQuery();
    function getFullName(params) {
        return `${params.row.client.first_name || ''} ${params.row.client.last_name || ''}`;
    }
    function setFullName(params) {
        const [firstName, lastName] = params.value.toString().split(' ');
        return { ...params.client.row, firstName, lastName };
    }
    const columns = [
        { field: 'id' },
        { field: 'inv_no', headerName: 'Invoice No', editable: false, width: 100 },
        { field: 'fullName', headerName: 'Client Name', editable: true, width: 150, valueGetter: getFullName, valueSetter: setFullName },
        { field: 'invoice_amount', headerName: 'Invoice Amount', width: 200 },
        { field: 'invoice_date', headerName: 'Invoice Date', width: 100 }
    ];
    return (
        <MainCard
            title="Invoice List"
            secondary={
                <Stack direction="row" spacing={2} justifyContent="space-between" alignItems="baseline" sx={{ mb: { xs: -0.5, sm: 0.5 } }}>
                    <Link className="btn btn-primary" to="/invoice/create">
                        New Invoice
                    </Link>
                </Stack>
            }
        >
            <div style={{ height: 700, width: '100%' }}>
                <DataGrid
                    rows={invoices}
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
export default InvoiceList;
