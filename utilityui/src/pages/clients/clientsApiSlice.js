import { apiSlice } from '../../api/apiSlice';

export const clientsApiSlice = apiSlice.injectEndpoints({
    endpoints: (builder) => ({
        getClients: builder.query({
            query: () => '/clients',
            providesTags: ['Clients']
            // keepUnusedDataFor: 60
        }),
        getClient: builder.query({
            query: (clientId) => `/client/${clientId}`
        }),
        addNewClient: builder.mutation({
            query: (initialClient) => ({
                url: '/clients/',
                method: 'POST',
                body: initialClient
            }),
            invalidatesTags: ['Clients']
        }),
        updatePost: builder.mutation({
            query(data) {
                const { id, ...body } = data;
                return {
                    url: `post/${id}`,
                    method: 'PUT',
                    body
                };
            },
            // Invalidates all queries that subscribe to this Post `id` only.
            // In this case, `getPost` will be re-run. `getPosts` *might*  rerun, if this id was under its results.
            invalidatesTags: (result, error, { id }) => [{ type: 'Posts', id }]
        }),
        getCategories: builder.query({
            query: () => '/client/categories',
            providesTags: ['Categories']
        }),
        addNewCategory: builder.mutation({
            query: (initialCategory) => ({
                url: '/client/categories/',
                method: 'POST',
                body: initialCategory
            }),
            invalidatesTags: ['Categories']
        })
    })
});

export const {
    useGetClientsQuery,
    useGetClientQuery,
    useAddNewClientMutation,
    useGetCategoriesQuery,
    useAddNewCategoryMutation
} = clientsApiSlice;
