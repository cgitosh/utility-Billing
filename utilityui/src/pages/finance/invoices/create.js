import * as React from 'react';
import TextField from '@mui/material/TextField';
import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
// project imports
import MainCard from 'components/MainCard';
import { useTheme } from '@mui/material/styles';
import { useEffect, useState, useRef } from 'react';
import { useAddNewInvoiceMutation } from './invoiceApiSlice';
import { useGetClientsQuery } from 'pages/clients/clientsApiSlice';
import { selectCurrentBusiness, selectCurrentUser } from 'pages/authentication/authSlice';
import {
    Button,
    Box,
    FormHelperText,
    Typography,
    Grid,
    Stack,
    Divider,
    FormControl,
    FormControlLabel,
    useMediaQuery,
    InputLabel,
    OutlinedInput,
    Select,
    MenuItem,
    MenuList,
    Autocomplete
} from '@mui/material';
import AnimateButton from 'components/@extended/AnimateButton';
// third party
import * as Yup from 'yup';
import { Formik } from 'formik';

export default function CreateInvoice() {
    const theme = useTheme();
    const matchDownSM = useMediaQuery(theme.breakpoints.down('md'));
    const User = useSelector(selectCurrentUser);
    const business = useSelector(selectCurrentBusiness);
    const navigate = useNavigate();
    const { data: clients = [], isLoading, isSuccess, isError, error } = useGetClientsQuery();
    const [addNewInvoice] = useAddNewInvoiceMutation();
    const handleSubmit = async (values) => {
        try {
            const invoice_amount = values.invoice_amount;
            const client = values.client;
            const Business = business.id;
            const user = User.id;
            await addNewInvoice({ ...values });
        } catch (err) {
            console.log('Invoice not added', err);
        }
    };
    return (
        <MainCard title="Create Invoice">
            <Formik
                initialValues={{
                    client: '',
                    invoice_amount: '',
                    invoice_balance: 0,
                    user: '',
                    Business: '',
                    submit: null
                }}
                validationSchema={Yup.object().shape({
                    client: Yup.string().required('Mobile is required'),
                    invoice_amount: Yup.string().required('House number is required')
                })}
                onSubmit={async (values, { setErrors, setStatus, setSubmitting }) => {
                    try {
                        setStatus({ success: true });
                        values.user = User.id;
                        values.Business = business.id;
                        handleSubmit(values);
                        navigate(-1);
                        setSubmitting(false);
                    } catch (err) {
                        console.error(err);
                        setStatus({ success: false });
                        setErrors({ submit: err.message });
                        setSubmitting(false);
                    }
                }}
            >
                {({ errors, handleBlur, handleChange, setFieldValue, handleSubmit, isSubmitting, touched, values }) => (
                    <form noValidate onSubmit={handleSubmit}>
                        <Grid container spacing={3}>
                            <Grid item xs={12} md={6}>
                                <FormControl
                                    fullWidth
                                    error={Boolean(touched.client && errors.client)}
                                    sx={{ ...theme.typography.customInput }}
                                >
                                    <InputLabel htmlFor="outlined-adornment-client-register">Client</InputLabel>
                                    <Select
                                        id="outlined-adornment-client-register"
                                        value={values.client}
                                        name="client"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        inputProps={{}}
                                    >
                                        {clients.map((Client) => (
                                            <MenuItem key={Client.id} value={Client.id}>
                                                {Client.first_name}
                                            </MenuItem>
                                        ))}
                                    </Select>
                                    {touched.client && errors.client && (
                                        <FormHelperText error id="standard-weight-helper-text--register">
                                            {errors.client}
                                        </FormHelperText>
                                    )}
                                </FormControl>
                            </Grid>
                            <Grid item xs={12} md={6}>
                                <FormControl
                                    fullWidth
                                    error={Boolean(touched.invoice_amount && errors.invoice_amount)}
                                    sx={{ ...theme.typography.customInput }}
                                >
                                    <InputLabel htmlFor="outlined-adornment-invoice_amount-register">Invoice Amount</InputLabel>
                                    <OutlinedInput
                                        id="outlined-adornment-invoice_amount-register"
                                        type="text"
                                        value={values.invoice_amount}
                                        name="invoice_amount"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        inputProps={{}}
                                    />
                                    {touched.invoice_amount && errors.invoice_amount && (
                                        <FormHelperText error id="standard-weight-helper-text--register">
                                            {errors.invoice_amount}
                                        </FormHelperText>
                                    )}
                                </FormControl>
                            </Grid>
                            <Grid item xs={12} md={2}>
                                <Box sx={{ mt: 3 }}>
                                    <AnimateButton>
                                        <Button
                                            disableElevation
                                            disabled={isSubmitting}
                                            size="large"
                                            type="submit"
                                            variant="contained"
                                            color="primary"
                                        >
                                            Save
                                        </Button>
                                    </AnimateButton>
                                </Box>
                            </Grid>
                            <Grid item xs={12} md={2}>
                                <Box sx={{ mt: 3 }}>
                                    <AnimateButton>
                                        <Button
                                            disableElevation
                                            disabled={isSubmitting}
                                            size="large"
                                            type="cancel"
                                            variant="contained"
                                            color="secondary"
                                        >
                                            Cancel
                                        </Button>
                                    </AnimateButton>
                                </Box>
                            </Grid>
                        </Grid>
                    </form>
                )}
            </Formik>
        </MainCard>
    );
}
