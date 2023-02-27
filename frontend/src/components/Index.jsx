import * as React from 'react';
import axios from 'axios';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
const design = createTheme();
export default function Index() {
    const [data, setData] = React.useState(null);

    const getNotification = () =>{
      axios.post('http://127.0.0.1:8000/notification').then(data => setData("Email sent successfully"))
    }
  return (
    <ThemeProvider theme={design}>
      <CssBaseline />
      <AppBar position="relative">
        <Toolbar>
          <Typography variant="h6" color="inherit" noWrap>
            Home
          </Typography>
        </Toolbar>
      </AppBar>
      <main>
        <Box
          sx={{
            bgcolor: 'background.paper',
            pt: 8,
            pb: 6,
          }}
        >
          <Container maxWidth="lg">
            <Typography
              component="h2"
              variant="h4"
              align="center"
              color="text.primary"
              gutterBottom
            >
              Email sending mechanism to notify the admin point of contact.  
            </Typography>
            <Stack
              sx={{ pt: 4 }}
              direction="row"
              spacing={2}
              justifyContent="center"
            >
              <Button variant="contained" onClick={getNotification}>Send Notification</Button>
            </Stack>

            <Typography variant="h2" align="center" color="text.secondary" paragraph>
                {data}
            </Typography>

          </Container>
        </Box>
      </main>
    </ThemeProvider>
  );
}