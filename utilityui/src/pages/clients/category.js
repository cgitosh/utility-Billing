import * as React from 'react';
import TextField from '@mui/material/TextField';
import { useNavigate } from 'react-router-dom';
// project imports
import MainCard from 'components/MainCard';
import { useTheme } from '@mui/material/styles';
import { useEffect, useState, useRef } from 'react';
import { useAddNewCategoryMutation } from './clientsApiSlice';
import { selectCurrentBusiness, selectCurrentUser } from 'pages/authentication/authSlice';
import {
    Button,
    Box,
    FormHelperText,
    Typography,
    Grid,
    Divider,
    FormControl,
    FormControlLabel,
    useMediaQuery,
    InputLabel,
    OutlinedInput,
    Select,
    MenuItem,
    MenuList
} from '@mui/material';
import AnimateButton from 'components/@extended/AnimateButton';
// third party
import * as Yup from 'yup';
import { Formik } from 'formik';
import { setUserAgent } from 'react-device-detect';
import { useSelector } from 'react-redux';
import NumberFormat from 'react-number-format';

export default function CreateCategory() {
    const theme = useTheme();
    const matchDownSM = useMediaQuery(theme.breakpoints.down('md'));
    const [addNewCategory, { isLoading }] = useAddNewCategoryMutation();
    const User = useSelector(selectCurrentUser);
    const business = useSelector(selectCurrentBusiness);
    const navigate = useNavigate();
    function NumberField({ OutlinedInput }) {
        return <NumberFormat {...OutlinedInput} thousandSeparator={true} prefix={'Ksh '} allowNegative={false} />;
    }
    const handleSubmit = async (values) => {
        try {
            const category_name = values.category_name;
            const monthly_charge = values.monthly_charge;
            const Business = business.id;
            const user = User.id;

            await addNewCategory({ category_name, monthly_charge, Business, user });
        } catch (err) {
            console.log('Category not added', err);
        }
    };
    return (
        <MainCard title="Add Client Category">
            <Formik
                initialValues={{
                    category_name: '',
                    monthly_charge: '',
                    submit: null
                }}
                validationSchema={Yup.object().shape({
                    category_name: Yup.string().required('Category name is required'),
                    monthly_charge: Yup.string().required('Monthly Charge is required')
                })}
                onSubmit={async (values, { setErrors, setStatus, setSubmitting }) => {
                    try {
                        setStatus({ success: true });
                        // values.business = business;
                        // values.user = user;
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
                {({ errors, handleBlur, handleChange, handleSubmit, isSubmitting, touched, values }) => (
                    <form noValidate onSubmit={handleSubmit}>
                        <Grid container spacing={matchDownSM ? 0 : 2}>
                            <Grid item xs={8} md={8}>
                                <FormControl
                                    fullWidth
                                    error={Boolean(touched.category_name && errors.category_name)}
                                    sx={{ ...theme.typography.customInput }}
                                >
                                    <InputLabel htmlFor="outlined-adornment-category_name-register">Category Name</InputLabel>
                                    <OutlinedInput
                                        id="outlined-adornment-category_name-register"
                                        type="text"
                                        value={values.category_name}
                                        name="category_name"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        inputProps={{}}
                                    />
                                    {touched.category_name && errors.category_name && (
                                        <FormHelperText error id="standard-weight-helper-text--register">
                                            {errors.category_name}
                                        </FormHelperText>
                                    )}
                                </FormControl>
                            </Grid>
                            <Grid item xs={12} md={8}>
                                <FormControl
                                    fullWidth
                                    error={Boolean(touched.monthly_charge && errors.monthly_charge)}
                                    sx={{ ...theme.typography.customInput }}
                                >
                                    <InputLabel htmlFor="outlined-adornment-monthly_charge-register">Monthly Charge</InputLabel>
                                    <NumberFormat
                                        id="outlined-adornment-monthly_charge-register"
                                        type="text"
                                        value={values.monthly_charge}
                                        thousandSeparator={true}
                                        prefix={'Ksh '}
                                        allowNegative={false}
                                        name="monthly_charge"
                                        onBlur={handleBlur}
                                        onChange={handleChange}
                                        inputProps={{}}
                                    />
                                    {touched.monthly_charge && errors.monthly_charge && (
                                        <FormHelperText error id="standard-weight-helper-text--register">
                                            {errors.monthly_charge}
                                        </FormHelperText>
                                    )}
                                </FormControl>
                            </Grid>
                        </Grid>
                        <Box sx={{ mt: 2 }}>
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
                    </form>
                )}
            </Formik>
        </MainCard>
    );
}
