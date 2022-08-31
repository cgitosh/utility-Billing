import * as React from 'react';
import TextField from '@mui/material/TextField';
import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
// project imports
import MainCard from 'components/MainCard';
import { useTheme } from '@mui/material/styles';
import { useEffect, useState, useRef } from 'react';
import { useAddNewClientMutation, useGetCategoriesQuery } from './clientsApiSlice';
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

export default function CreateClient() {
    const theme = useTheme();
    const matchDownSM = useMediaQuery(theme.breakpoints.down('md'));
    const User = useSelector(selectCurrentUser);
    const business = useSelector(selectCurrentBusiness);
    const navigate = useNavigate();
    const { data: categories = [], isLoading, isSuccess, isError, error } = useGetCategoriesQuery();
    const [addNewClient] = useAddNewClientMutation();
    const handleSubmit = async (values) => {
        try {
            const house_no = values.house_no;
            const category = values.category;
            const Business = business.id;
            const user = User.id;

            await addNewClient({ ...values });
        } catch (err) {
            console.log('Client not added', err);
        }
    };
    return (
        <MainCard title="Add Client">
            <Formik
                initialValues={{
                    first_name: '',
                    last_name: '',
                    house_no: '',
                    category: '',
                    mobile_no: '',
                    address: '',
                    user: '',
                    Business: '',
                    submit: null
                }}
                validationSchema={Yup.object().shape({
                    mobile_no: Yup.string().required('Mobile is required'),
                    house_no: Yup.string().required('House number is required'),
                    first_name: Yup.string().required('First name is required')
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
                                <Stack spacing={1}>
                                    <FormControl
                                        fullWidth
                                        error={Boolean(touched.first_name && errors.first_name)}
                                        sx={{ ...theme.typography.customInput }}
                                    >
                                        <InputLabel htmlFor="outlined-adornment-first_name-register">First Name</InputLabel>
                                        <OutlinedInput
                                            id="outlined-adornment-first_name-register"
                                            type="text"
                                            value={values.first_name}
                                            name="first_name"
                                            onBlur={handleBlur}
                                            onChange={handleChange}
                                            inputProps={{}}
                                        />
                                        {touched.first_name && errors.first_name && (
                                            <FormHelperText error id="standard-weight-helper-text--register">
                                                {errors.first_name}
                                            </FormHelperText>
                                        )}
                                    </FormControl>
                                </Stack>
                            </Grid>
                            <Grid item xs={12} sm={6}>
                                <Stack spacing={1}>
                                    <FormControl
                                        fullWidth
                                        error={Boolean(touched.last_name && errors.last_name)}
                                        sx={{ ...theme.typography.customInput }}
                                    >
                                        <InputLabel htmlFor="outlined-adornment-lname-register">Last Name</InputLabel>
                                        <OutlinedInput
                                            id="outlined-adornment-lname-register"
                                            type="text"
                                            value={values.last_name}
                                            name="last_name"
                                            onBlur={handleBlur}
                                            onChange={handleChange}
                                            inputProps={{}}
                                        />
                                        {touched.last_name && errors.last_name && (
                                            <FormHelperText error id="standard-weight-helper-text--register">
                                                {errors.last_name}
                                            </FormHelperText>
                                        )}
                                    </FormControl>
                                </Stack>
                            </Grid>
                            <Grid item xs={12} md={6}>
                                <Stack spacing={1}>
                                    <FormControl
                                        fullWidth
                                        error={Boolean(touched.house_no && errors.house_no)}
                                        sx={{ ...theme.typography.customInput }}
                                    >
                                        <InputLabel htmlFor="outlined-adornment-house_no-register">House Number</InputLabel>
                                        <OutlinedInput
                                            id="outlined-adornment-house_no-register"
                                            type="text"
                                            value={values.house_no}
                                            name="house_no"
                                            onBlur={handleBlur}
                                            onChange={handleChange}
                                            inputProps={{}}
                                        />
                                        {touched.house_no && errors.house_no && (
                                            <FormHelperText error id="standard-weight-helper-text--register">
                                                {errors.house_no}
                                            </FormHelperText>
                                        )}
                                    </FormControl>
                                </Stack>
                            </Grid>
                            <Grid item xs={12} md={6}>
                                <FormControl
                                    fullWidth
                                    error={Boolean(touched.address && errors.address)}
                                    sx={{ ...theme.typography.customInput }}
                                >
                                    <InputLabel htmlFor="outlined-adornment-address-register">Location Address</InputLabel>
                                    <OutlinedInput
                                        id="outlined-adornment-address-register"
                                        type="text"
                                        value={values.address}
                                        name="address"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        inputProps={{}}
                                    />
                                    {touched.address && errors.address && (
                                        <FormHelperText error id="standard-weight-helper-text--register">
                                            {errors.address}
                                        </FormHelperText>
                                    )}
                                </FormControl>
                            </Grid>
                            <Grid item xs={12} md={6}>
                                <FormControl
                                    fullWidth
                                    error={Boolean(touched.category && errors.category)}
                                    sx={{ ...theme.typography.customInput }}
                                >
                                    <InputLabel htmlFor="outlined-adornment-category-register">Category</InputLabel>
                                    <Select
                                        id="outlined-adornment-Crew_category-register"
                                        value={values.category}
                                        name="category"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        inputProps={{}}
                                    >
                                        {categories.map((Category) => (
                                            <MenuItem key={Category.id} value={Category.id}>
                                                {Category.category_name}
                                            </MenuItem>
                                        ))}
                                    </Select>
                                    {touched.category && errors.category && (
                                        <FormHelperText error id="standard-weight-helper-text--register">
                                            {errors.category}
                                        </FormHelperText>
                                    )}
                                </FormControl>
                            </Grid>
                            <Grid item xs={12} md={6}>
                                <FormControl
                                    fullWidth
                                    error={Boolean(touched.mobile_no && errors.mobile_no)}
                                    sx={{ ...theme.typography.customInput }}
                                >
                                    <InputLabel htmlFor="outlined-adornment-mobile_no-register">Mobile No</InputLabel>
                                    <OutlinedInput
                                        id="outlined-adornment-mobile_no-register"
                                        type="text"
                                        value={values.mobile_no}
                                        name="mobile_no"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        inputProps={{}}
                                    />
                                    {touched.mobile_no && errors.mobile_no && (
                                        <FormHelperText error id="standard-weight-helper-text--register">
                                            {errors.mobile_no}
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
