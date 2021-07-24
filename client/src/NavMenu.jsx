import { Box, Flex, HStack, Img } from '@chakra-ui/react';
import * as React from 'react';
import {
  HiDuplicate,
  HiInformationCircle,
  HiRefresh,
  HiTemplate,
} from 'react-icons/hi';
import AcademicIcon from './assets/svg/AcademicIcon.svg';

import { NavItem } from './NavItem';

const MobileNavMenu = props => {
  const { isOpen } = props;
  return (
    <Flex
      hidden={!isOpen}
      as="nav"
      direction="column"
      bg="blue.600"
      position="fixed"
      height="calc(100vh - 4rem)"
      top="16"
      insetX="0"
      zIndex={10}
      w="full"
    >
      <Box px="4">
        <NavItem.Mobile active label="About" />
        <NavItem.Mobile label="Content" />
      </Box>
    </Flex>
  );
};

const DesktopNavMenu = () => (
  <HStack
    spacing="3"
    flex="1"
    display={{
      base: 'none',
      lg: 'flex',
    }}
  >
    <NavItem.Desktop icon={<HiInformationCircle />} label="About" />
    <NavItem.Desktop
      active
      icon={<Img src={AcademicIcon} boxSize="4" />}
      label="Content"
    />
  </HStack>
);

export const NavMenu = {
  Mobile: MobileNavMenu,
  Desktop: DesktopNavMenu,
};
