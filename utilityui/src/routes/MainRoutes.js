import { Children, lazy } from 'react';

// project import
import Loadable from 'components/Loadable';
import MainLayout from 'layout/MainLayout';
import RequireAuth from 'pages/authentication/RequireAuth';
import { element, elementType } from 'prop-types';

// render - dashboard
const DashboardDefault = Loadable(lazy(() => import('pages/dashboard')));

// Clients routing
const ClientsList = Loadable(lazy(() => import('pages/clients/list')));
const CreateCategory = Loadable(lazy(() => import('pages/clients/category')));
const CreateClient = Loadable(lazy(() => import('pages/clients/create')));
// Invoice routing
const InvoiceList = Loadable(lazy(() => import('pages/finance/invoices/list')));
const CreateInvoice = Loadable(lazy(() => import('pages/finance/invoices/create')));

// render - utilities
const Typography = Loadable(lazy(() => import('pages/components-overview/Typography')));
const Color = Loadable(lazy(() => import('pages/components-overview/Color')));
const Shadow = Loadable(lazy(() => import('pages/components-overview/Shadow')));
const AntIcons = Loadable(lazy(() => import('pages/components-overview/AntIcons')));

// ==============================|| MAIN ROUTING ||============================== //
/* protected routes */
const MainRoutes = {
    path: '/',
    element: <RequireAuth />,
    children: [
        {
            path: '/',
            element: <MainLayout />,
            children: [
                {
                    path: '/dashboard/default',
                    element: <DashboardDefault />
                },
                {
                    path: '/',
                    element: <DashboardDefault />
                },
                {
                    path: '/clients',
                    element: <ClientsList />
                },
                {
                    path: '/client/category',
                    element: <CreateCategory />
                },
                {
                    path: '/client/create',
                    element: <CreateClient />
                },
                {
                    path: '/invoices',
                    element: <InvoiceList />
                },
                {
                    path: '/invoice/create',
                    element: <CreateInvoice />
                },
                {
                    path: 'color',
                    element: <Color />
                }
            ]
        }
    ]
};

export default MainRoutes;
