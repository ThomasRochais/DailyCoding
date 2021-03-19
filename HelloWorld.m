'Hello, World'

% Clear any prior session
clc       % Clear screen
clear all % Clear variables
close all % Close trends

% Get version and list available toolboxes
% ver

% Get help on a particular function
% help max

% Create a new variable
b = 0.5

% Generatte a 10 x 4 matrix of random numbers
M = rand(10,4); % Use a semi-colon to suppress output

% Display a variable
disp(M)

% Compute the Standard Deviation for each column
std(M)

% Compute Max and Min Values for each column
max(M)
min(M)

% Compute Average over all data
avg = mean(mean(M))

%If, Elseif, Else Statement
if avg > 0.5
    disp(['Average over 0.5: ' num2str(avg)])
elseif avg == 0.5
    'Average is exactly 0.5'
else
    disp(['Average below 0.5: ' num2str(avg)])
end

% For looop
isum = 0;
for i = 1:10
    isum = isum + 1;
end
isum

% Function example
result = myFunction(isum)

% Create a trend of the first data column
plot(M(:,1))

function y = myFunction(x)
y = x + 2;
end
