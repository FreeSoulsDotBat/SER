import { SafeAreaView, View } from 'react-native'
import { NavigationContainer } from '@react-navigation/native'
import Stack from './Stack'
import { colors } from '../theme/colors'

const Theme = {
	dark: false,
	colors: colors,
	components: {
		button: {
			color: 'black',
		},
	},
}

export default App = () => {
	return (
		<SafeAreaView style={{ flex: 1 }}>
			<NavigationContainer theme={Theme}>
				<Stack />
			</NavigationContainer>
		</SafeAreaView>
	)
}
