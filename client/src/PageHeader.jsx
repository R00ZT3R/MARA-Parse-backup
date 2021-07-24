import {
  Box,
  Container,
  Heading,
  Stack,
  useColorModeValue,
} from '@chakra-ui/react';
import * as React from 'react';
import { TabLink } from './TabLink';

export const PageHeader = props => (
  <Box
    bg={useColorModeValue('white', 'gray.900')}
    pt="8"
    shadow="sm"
    {...props}
  >
    <Container maxW="7xl">
      <Heading size="lg" mb="3">
        Add Content
      </Heading>
    </Container>
  </Box>
);
