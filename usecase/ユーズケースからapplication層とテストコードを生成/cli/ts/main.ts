import { UserRegisterCommand, UserApplicationService } from './server/User/UserApplicationService';
import { InMemmoryUserRepository } from './server/User/User';
const command = new UserRegisterCommand();
const service = new UserApplicationService(new InMemmoryUserRepository());
service.register(command);