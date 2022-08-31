// assets
import {
    AppstoreAddOutlined,
    AntDesignOutlined,
    BarcodeOutlined,
    BgColorsOutlined,
    FontSizeOutlined,
    LoadingOutlined,
    BookOutlined,
    UserOutlined
} from '@ant-design/icons';

// icons
const icons = {
    FontSizeOutlined,
    BgColorsOutlined,
    BarcodeOutlined,
    AntDesignOutlined,
    LoadingOutlined,
    AppstoreAddOutlined,
    BookOutlined,
    UserOutlined
};

// ==============================|| MENU ITEMS - Operations ||============================== //

const operations = {
    id: 'operations',
    title: 'operations',
    type: 'group',
    children: [
        {
            id: 'ops-clients',
            title: 'Clients',
            type: 'item',
            url: '/clients',
            icon: icons.UserOutlined
        },
        {
            id: 'fin-invoices',
            title: 'Invoices',
            type: 'item',
            url: '/invoices',
            icon: icons.BookOutlined
        }
    ]
};

export default operations;
