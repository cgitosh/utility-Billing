import { apiSlice } from '../../../api/apiSlice';

export const invoiceApiSlice = apiSlice.injectEndpoints({
    endpoints: (builder) => ({
        getInvoices: builder.query({
            query: () => '/invoices',
            providesTags: ['Invoices']
            // keepUnusedDataFor: 60
        }),
        getInvoice: builder.query({
            query: (clientId) => `/invoice/${invoiceId}`
        }),
        addNewInvoice: builder.mutation({
            query: (initialInvoice) => ({
                url: '/invoices/',
                method: 'POST',
                body: initialInvoice
            }),
            invalidatesTags: ['Invoices']
        })
    })
});
export const { useGetInvoicesQuery, useGetInvoiceQuery, useAddNewInvoiceMutation } = invoiceApiSlice;
